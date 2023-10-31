class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    #it has a children attribute
    #it will be a tree
    #we can do preorder traversal: root left right (depth first)
    #we can do inorder traversal: left root right
    #we can do postorder traversal: left right root
    #it is recommended to start with the root so preorder
    #alternatively we can go down by levels...
    #return self.breadthFirstGetElementById(id);
    return self.preorderGetElementById(id);


  def preorderMainGetElementById(self, id, snd):
    #root left right
    #or rather root then kid a then its kids...
    #snd = root
    #snd = root.kids[0]
    #snd = root.kids[0].kids[0]
    #...
    #until it runs out of kids then it moves on to the next one and so on ...
    if (snd == None): return None;
    elif (snd["id"] == id): return snd;
    else:
      if (len(snd["children"]) < 1): return None;
      else:
        for kid in snd["children"]:
          retval = self.preorderMainGetElementById(id, kid);
          if (retval == None): pass;
          else: return retval;
    return None;

  def preorderGetElementById(self, id):
    return self.preorderMainGetElementById(id, self.root);

  def breadthFirstGetElementById(self, id):
    #goes by level
    #the root then all of its kids then their kids kids...
    #vlist or determine the next level
    #root, then its kids, then their kids, then their kids' kids...
    nxtnds = [self.root];
    #print(nxtnds);
    i = 0;
    while(0 < len(nxtnds) and i < len(nxtnds)):
      #print(f"i = {i}");
      nd = nxtnds[i];
      #print(f"nd[id] = {nd['id']}");
      #print(f"nd[tag_name] = {nd['tag_name']}");
      if (nd["id"] == id): return nd;
      else:
        if (len(nd["children"]) < 1): pass;
        else:
          for kd in nd["children"]: nxtnds.append(kd);
        nxtnds.remove(nxtnds[0]);
        i -= 1;
        #print(nxtnds);
        #print(f"NEW i = {i}");
        #print(f"NEW LEN(nxtnds) = {len(nxtnds)}");
      i += 1;
    return None;
