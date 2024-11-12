# Inventory Graph



## Nodes (=Activities)

### How do I iterate over nodes in a `Database`?

```python
for node in bd.Database('<database_name>'):
    do_something(node)
```

Iteration over nodes is helpful for complicated filter cases:

```python
[
    node for node in bd.Database('<database_name>')
    if 'electricity production' in node['name']
    and 'coal' in node['name']
    and node['location'].lower() == 'de'
]
```

### How do I get a random node from a `Database`?

```python
bd.Database('<database_name>').random()
```

### How do I get a specific node?

```python
my_node = bd.get_node(my_attr="<some_value>")
```

You can pass in any attribute value, including "database" and "code". Combine multiple filters with commas, e.g. `bd.get_node(name="<foo>", location="bar")`. To search for attribute keys with spaces, use a dictionary: `bd.get_node(**{"some value with spaces": True})`.

### How do I create a new node?

```python
my_node = bd.Database('<database_name>').new_node(**attributes)
my_node.save()
```

Where `attributes` is a dictionary of the desired node attributes.

### How do I get all the data attributes of a node?

```python
my_node.as_dict()
```

### How do I change data attributes of a node?

```python
my_node['<some_key>'] = "<some_new_value>"
my_node.save()
```

## Edges (=Exchanges)

### How do I list edges of a process where inputs are consumed?

```python
list(my_node.technosphere())
```

### How do I list edges of a process where outputs are produced?

```python
list(my_node.production())
```

### How do I list all edges which consume the node `my_node`?

```python
list(my_node.consumers())
```

### How do I list all biosphere edges of a process?

```python
list(my_node.biosphere())
```

### How do I list all edges defined on a process?

```python
list(my_node.edges())
```

You can use a [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) to iterate over the edges to do more complex filtering:

```python
[
    edge for edge in my_node.edges()
    if 'car' in edge.input['name']
]
```

### How do I delete an edge?

```python
my_edge.delete()
```

### How do I get all the data attributes of an edge?

```python
my_edge.as_dict()
```

### How do I access the input and output nodes of an edge?

```python
my_edge.input
my_edge.output
```

### How do I change the input or output of an edge?

```python
my_edge.input = new_node
my_edge.output = new_node
my_edge.save()
```

### How do I change data attributes of an edge?

```python
my_edge['<some_key>'] = "<some_new_value>"
my_edge.save()
```

### How do I create a new edge?

```python
my_edge = my_node.new_edge(**attributes)
my_edge.save()
```

Where `attributes` are the desired attributes of the edge; must include `type`, `amount`, and `input`.
