module Aoc.Y2021.Day06 where

import Data.Text (unpack, pack, splitOn)

newtype Lanternfish = Fish Integer deriving (Show, Eq, Ord)

parse :: String -> [Lanternfish]
parse s = map (Fish . read . unpack) (splitOn (pack "," ) (pack s))

-- TASK 1:
nextDay :: Lanternfish -> [Lanternfish]
nextDay (Fish 0) = [Fish 6, Fish 8]
nextDay (Fish timer) = [Fish (timer - 1)]

stepNDays :: [Lanternfish] -> Int -> [Lanternfish]
stepNDays list n = iterate (concatMap nextDay) list !! n

-- TASK 2
count :: Eq a => a -> [a] -> Int
count n l = length $ filter (== n) l

countTimer :: [Lanternfish] -> [Lanternfish] -> [Int]
countTimer xs l = map (`count` l) xs

shiftL :: Int -> [a] -> [a]
shiftL 0 xs = xs
shiftL n xs
    | n < 0 = error "negative index"
    | otherwise = drop n xs ++ take n xs

replaceNth :: Int -> a -> [a] -> [a]
replaceNth _ _ [] = []
replaceNth n newVal xs = front ++ newVal:back
    where (front, nth:back) = splitAt n xs 

stepDay :: [Int] -> [Int]
stepDay xs = let newL = shiftL 1 xs in 
    replaceNth 6 ((newL !! 6) + (newL !! 8)) newL

getPopulationAfterN :: [Lanternfish] -> Int -> Int
getPopulationAfterN list n = sum (iterate stepDay (countTimer toCount list) !! n)
    where toCount = [Fish 0, Fish 1, Fish 2, Fish 3, Fish 4, Fish 5, Fish 6, Fish 7, Fish 8] 

main :: IO()
main = do
    contents <- readFile "inputs\\Day06.txt"
    let input = parse contents
    -- print $ length $ stepNDays input 80
    print $ getPopulationAfterN input 80
    print $ getPopulationAfterN input 256