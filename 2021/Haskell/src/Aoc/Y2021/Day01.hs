module Aoc.Y2021.Day01 where

-- TASK 1
sumElements :: Num b => [b] -> b
sumElements [] = 0
sumElements (x:xs) = sum (x:xs)

convertList :: (Ord a1, Num a2) => [a1] -> [a2]
convertList [] = []
convertList [x] = []
convertList (x:(y:ys)) = increased [x,y] : convertList (y:ys)

increased :: (Ord a, Num p) => [a] -> p
increased [] = 0
increased [x] = 0
increased (x:(y:ys)) = if x < y then 1 else 0

-- TASK 2
groupList :: Num a => [a] -> [a]
groupList [] = []
groupList [x] = [x]
groupList (x:[y]) = [x+y]
groupList (x:(y:(z:zs))) = (x+y+z) : groupList (y:(z:zs))

-- MAIN
main :: IO ()
main = do
   contents <- readFile "inputs\\Day01.txt"
   print . sumElements . convertList . groupList . map readInt . words $ contents

readInt :: String -> Int
readInt = read
