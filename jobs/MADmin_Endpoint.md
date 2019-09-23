# MADmin Endpoint for Jobs returnings

All returning Values from jobs (manual or automatic started) will add to a new MADMin Endpoint

## Endpoint URL

**MADminip:port**/jobstatus

## Returning

**JSON Format**

Example:

```buildoutcfg
{  
   "m7":{  
      "POGODROID_Version":"[versionName=1.1.3.0]",
      "POGO_Version":"[versionName=0.153.2]",
      "RGC_Version":"[versionName=1.9.3, versionName=1.8.34]"
   }
}
```

Each device will be added as own object.