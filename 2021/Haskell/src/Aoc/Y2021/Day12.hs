module Aoc.Y2021.Day12 where

import Text.Parsec.Text (Parser)
import Text.Parsec (string, many, letter, upper, (<|>), char, lower, parse, try)
import Data.Map (Map, empty, insertWith, lookup, toList)
import Data.Text (pack)
import Data.Map.Internal.Debug (showTree)

data Cave = Start String
    | End String
    | Small String
    | Big String
    deriving (Eq, Ord, Show)

type Edge = (Cave, Cave)

type Path = [Cave]

-- Parsers for caves
startP :: Parser Cave
startP = do
    x <- string "start"
    return $ Start x

endP :: Parser Cave
endP = do
    x <- string "end"
    return $ End x

smallP :: Parser Cave
smallP = do
    x <- lower
    ys <- many letter
    return $ Small $ x:ys

bigP :: Parser Cave
bigP = do
    x <- upper
    ys <- many letter
    return $ Big $ x:ys

caveP :: Parser Cave
caveP = do
    try startP <|> try endP <|> smallP <|> bigP

edgeP :: Parser Edge
edgeP = do
    x <- caveP
    _ <- char '-'
    y <- caveP
    return (x,y)

buildSystem :: [Edge] -> Map Cave [Cave] -> Map Cave [Cave]
buildSystem [] m = m
buildSystem (x:xs) m = buildSystem xs $ insertWith f (snd x) [fst x] $ insertWith f (fst x) [snd x] m
    where f new_value old_value = new_value ++ old_value

collectEdges :: [String] -> [Edge]
collectEdges [] = []
collectEdges (x:xs) = y : collectEdges xs
    where Right y = parse edgeP "" (pack x)

{- 
Algorithm outline:
1. Get all adjacent Caves to start Cave
2. For each findPath to end (not containing 2 small caves)
findPaths :: Cave -> Cave -> Map Cave [Cave] -> [Path]
findPaths start end m
    | start == end = []
    | otherwise = f xs
    where 
        Just xs = Data.Map.lookup start m
        f (x:xs) = filter smallCountLegal (findPaths x end m) ++ f xs
        f [] = []
-}

smallCountLegal :: Path -> Bool
smallCountLegal xs = length (filter isSmall xs) < 2

isSmall :: Cave -> Bool
isSmall (Small x) = True
isSmall _ = False

main :: IO()
main = do
    contents <- readFile "inputs\\example12.txt"
    let input = lines contents
    let edges = buildSystem (collectEdges input) empty
    print $ toList edges



