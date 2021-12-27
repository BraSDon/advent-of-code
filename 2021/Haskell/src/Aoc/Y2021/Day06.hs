module Aoc.Y2021.Day06 where

import Data.Text (unpack, pack, splitOn)

newtype Lanternfish = Fish Integer deriving (Show, Eq)

parse :: String -> [Lanternfish]
parse s = map (Fish . read . unpack) (splitOn (pack "," ) (pack s))

nextDay :: Lanternfish -> [Lanternfish]
nextDay (Fish 0) = [Fish 6, Fish 8]
nextDay (Fish timer) = [Fish (timer - 1)]

stepNDays :: [Lanternfish] -> Int -> [Lanternfish]
stepNDays list n = iterate (concatMap nextDay) list !! n 

main :: IO()
main = do
    contents <- readFile "inputs\\Day06.txt"
    let input = parse contents 
    print $ length $ stepNDays input 80
    print $ length $ stepNDays input 256