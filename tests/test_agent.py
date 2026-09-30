import unittest
from agent import analyze
def p(): return {"now":"2026-09-29T10:00:00Z","incidents":[{"id":"I","started_at":"2026-09-29T09:30:00Z","target_minutes":60}]}
class Tests(unittest.TestCase):
 def test_within(self): self.assertEqual(analyze(p())["status"],"within_sla")
 def test_age(self): self.assertEqual(analyze(p())["incidents"][0]["age_minutes"],30)
 def test_breach(self): x=p(); x["incidents"][0]["target_minutes"]=20; self.assertEqual(analyze(x)["status"],"breached")
 def test_ids(self): self.assertEqual(analyze(p())["breached_ids"],[])
 def test_future(self): x=p(); x["incidents"][0]["started_at"]="2026-09-29T11:00:00Z"; self.assertEqual(analyze(x)["incidents"][0]["age_minutes"],0)
 def test_naive(self): x=p(); x["now"]="2026-09-29T10:00:00"; self.assertRaises(ValueError,analyze,x)
 def test_bad_target(self): x=p(); x["incidents"][0]["target_minutes"]=-1; self.assertRaises(ValueError,analyze,x)
 def test_bad_shape(self): self.assertRaises(ValueError,analyze,{"now":p()["now"],"incidents":[{}]})
 def test_bool_target(self): x=p(); x["incidents"][0]["target_minutes"]=True; self.assertRaises(ValueError,analyze,x)
 def test_duplicate(self): x=p(); x["incidents"].append(x["incidents"][0]); self.assertRaises(ValueError,analyze,x)
if __name__=="__main__": unittest.main()
