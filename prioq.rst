PrioQ
##############################


MAD has the ability to make a 'on the fly' route calculation. The purpose of this is to enable routes to adapt to real-time events, f.i. a spawning event. A PrioQ will be generated based on the settings on the Area and will be performed out of the ordinary route. 

These are the setting in Area along side with an example value ():

- `delay_after_prioq_event`: (60) -Setting this to 0 will disable the use of PrioQ but not the generation of route. 
- `priority_queue_clustering_timedelta`: (300) - Will group up events within the timeframe to make the PrioQ more effective.
- `remove_from_queue_backlog`: (600) - Cuts off an possible backlog
 
