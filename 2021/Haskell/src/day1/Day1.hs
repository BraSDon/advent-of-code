module Day1 where

-- TASK 1
sumElements (x:xs) = foldr (+) 0 (x:xs)
  
convertList [x] = [] 
convertList (x:(y:ys)) = increased [x,y] : convertList (y:ys)
-- convertList (x:[y]) = [increased [x,y]]

increased (x:[y]) = if x < y then 1 else 0

-- TASK 2
groupList [x] = [x]
groupList (x:[y]) = [x+y]
groupList (x:(y:(z:zs))) = (x+y+z) : (groupList (y:(z:zs)))

-- MAIN
main :: IO ()
main = do 
   contents <- readFile "day1.txt"
   print . sumElements . convertList . groupList . map readInt . words $ contents

readInt :: String -> Int
readInt = read
