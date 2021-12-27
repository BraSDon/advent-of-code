module Aoc.Y2021.Day07 where
import Data.Text (pack, unpack, splitOn)

parse :: String -> [Int]
parse s = map (read . unpack) (splitOn (pack "," ) (pack s))

metric1 :: Num c => c -> [c] -> c
metric1 pos = sum . map (\x -> abs(x - pos))

gaussSum :: Integral a => a -> a
gaussSum n = (n * (n + 1)) `div` 2

metric2 :: Integral c => c -> [c] -> c
metric2 pos = sum . map (\x -> gaussSum $ abs(x - pos))

main :: IO()
main = do
    contents <- readFile "inputs\\Day07.txt"
    let input = parse contents
    print $ minimum (map (`metric1` input) [minimum input.. maximum input])
    print $ minimum (map (`metric2` input) [minimum input.. maximum input])