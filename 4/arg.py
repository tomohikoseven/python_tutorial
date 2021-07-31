def concat(*args, sep="/"):
  print(args)
  return sep.join(args)

print( concat('a', 'b') )
print( concat('a', 'b', sep='.' ) )