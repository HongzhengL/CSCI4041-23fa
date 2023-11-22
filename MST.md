```
sort edges by weight into array Edge[1..E]
A[] = array of booleans of size E
        initially all false 
ds := disjoint set forest
for v := 1 to V do ds.makeset(v)
for e := 1 to E do
    if ds.find(Edge[e].start) != ds.find(Edge[e].end) then
        A[e] := true        # A ;= A union {e}
        ds.union(Edge[e].start, Edge[e].end)
ls := []
for e := 1 to E do
    if A[e] then ls.push(Edge[e])
return ls

```