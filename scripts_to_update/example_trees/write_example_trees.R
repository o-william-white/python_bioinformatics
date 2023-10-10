
library(ape)

seed<-123

for(i in 1:10){
  tre <- rtree(10, rooted = F, tip.label = paste0("sample", LETTERS[1:10]))
  write.tree(tre, paste0("example_tree_",i, ".newick"))
}

