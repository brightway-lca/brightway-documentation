What is the preferred method to calculate an LCA in BW25? What is the difference in using .get(), .get_activity(), or the key as a demand dictionary?

There are three ways (that I know of) to do this that work:

`act1 = bd.get_activity(("DBNAME","ACTIVITY_CODE"))`
`method = 'EF v3.1', 'climate change', 'global warming potential (GWP100)' `
`act1_lca = bc.LCA({act1:1}, method)`
... act1_lca.lci(), act1_lca.lcia(), print(act1_lca.score)

OR 

`act2 = bd.Database("DBNAME").get("ACTIVITY_CODE")`
`act2_lca = bc.LCA({act2:1}, method)`
... (.lci(), .lcia(), ...)


OR 

`act3 = bc.LCA({("DBNAME", "ACTIVITY_CODE"):1}, method)`
... (act3.lci(), .lcia(), ...)

