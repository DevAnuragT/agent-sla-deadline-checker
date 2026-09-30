"""Compare incident age with explicit SLA targets."""
from datetime import datetime, timezone
import math
def _time(v,n):
    if not isinstance(v,str): raise ValueError(n+" must be a timezone-aware ISO timestamp")
    try: x=datetime.fromisoformat(v[:-1]+"+00:00" if v.endswith("Z") else v)
    except ValueError: raise ValueError(n+" must be a timezone-aware ISO timestamp")
    if x.tzinfo is None: raise ValueError(n+" must include a timezone")
    return x.astimezone(timezone.utc)
def analyze(payload:dict)->dict:
    if not isinstance(payload,dict) or not isinstance(payload.get("incidents"),list): raise ValueError("incidents must be a list")
    now=_time(payload.get("now"),"now"); out=[]; seen=set()
    for item in payload["incidents"]:
        if not isinstance(item,dict) or set(item)!={"id","started_at","target_minutes"}: raise ValueError("invalid incident shape")
        if not isinstance(item["id"],str) or not item["id"].strip() or item["id"] in seen: raise ValueError("ids must be unique non-empty strings")
        target=item["target_minutes"]
        if isinstance(target,bool) or not isinstance(target,(int,float)) or not math.isfinite(float(target)) or target<0 or target>1e7: raise ValueError("target_minutes must be bounded")
        seen.add(item["id"]); started=_time(item["started_at"],"started_at"); age=max(0,(now-started).total_seconds()/60); breached=age>float(target)
        out.append({"id":item["id"],"age_minutes":round(age,3),"target_minutes":float(target),"breached":breached})
    return {"status":"breached" if any(x["breached"] for x in out) else "within_sla","breached_ids":[x["id"] for x in out if x["breached"]],"incidents":out,"basis":"caller-supplied now minus started_at compared with each target; future starts have zero age"}
