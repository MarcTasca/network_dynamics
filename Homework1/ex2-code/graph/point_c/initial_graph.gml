graph [
  directed 1
  node [
    id 0
    label "p1"
    color "blue"
    bipartite 0
    pos -1.0
    pos -0.75
  ]
  node [
    id 1
    label "p2"
    color "blue"
    bipartite 0
    pos -1.0
    pos -0.25
  ]
  node [
    id 2
    label "p3"
    color "blue"
    bipartite 0
    pos -1.0
    pos 0.24999999999999994
  ]
  node [
    id 3
    label "p4"
    color "blue"
    bipartite 0
    pos -1.0
    pos 0.75
  ]
  node [
    id 4
    label "b1"
    color "blue"
    bipartite 1
    pos 1.0
    pos -0.75
  ]
  node [
    id 5
    label "b2"
    color "blue"
    bipartite 1
    pos 1.0
    pos -0.25
  ]
  node [
    id 6
    label "b3"
    color "blue"
    bipartite 1
    pos 1.0
    pos 0.24999999999999994
  ]
  node [
    id 7
    label "b4"
    color "blue"
    bipartite 1
    pos 1.0
    pos 0.75
  ]
  node [
    id 8
    label "o"
    color "red"
    pos -2
    pos 0
  ]
  node [
    id 9
    label "d"
    color "green"
    pos 2
    pos 0
  ]
  edge [
    source 0
    target 4
    capacity 1
    flow 0
  ]
  edge [
    source 0
    target 5
    capacity 1
    flow 1
  ]
  edge [
    source 1
    target 5
    capacity 1
    flow 1
  ]
  edge [
    source 1
    target 6
    capacity 1
    flow 1
  ]
  edge [
    source 2
    target 4
    capacity 1
    flow 1
  ]
  edge [
    source 2
    target 7
    capacity 1
    flow 1
  ]
  edge [
    source 3
    target 4
    capacity 1
    flow 1
  ]
  edge [
    source 3
    target 5
    capacity 1
    flow 1
  ]
  edge [
    source 3
    target 7
    capacity 1
    flow 1
  ]
  edge [
    source 4
    target 9
    capacity 2
    flow 2
  ]
  edge [
    source 5
    target 9
    capacity 3
    flow 3
  ]
  edge [
    source 6
    target 9
    capacity 2
    flow 1
  ]
  edge [
    source 7
    target 9
    capacity 2
    flow 2
  ]
  edge [
    source 8
    target 0
    capacity +INF
    flow 1
  ]
  edge [
    source 8
    target 1
    capacity +INF
    flow 2
  ]
  edge [
    source 8
    target 2
    capacity +INF
    flow 2
  ]
  edge [
    source 8
    target 3
    capacity +INF
    flow 3
  ]
]
