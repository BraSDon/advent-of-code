module Aoc.Y2021.Day10 where

import Text.Parsec.Text ( Parser )
import Text.Parsec ( char, (<|>) )
import Data.Map (Map, fromList, lookup, findWithDefault)
import Data.List (sort)

{- Algorithm outline:
1. Iterate over input
2. Add opening brackets to list
3. If there is a closing bracket, it must match (Map) the last bracket added to the list
    True: Remove the last bracket added to the list
    False: -> corrupted
4. If the list is not empty by the end, 
then the missing brackets are the mapped brackets in the list in reversed order
-}

mapBrackets :: Map Char Char
mapBrackets = fromList [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]

mapPoints :: Map Char Int
mapPoints = fromList [(')', 3), (']', 57), ('}', 1197), ('>', 25137)]

mapPointsTask2 :: Map Char Int
mapPointsTask2 = fromList [(')', 1), (']', 2), ('}', 3), ('>', 4)]

isOpening :: Char -> Bool
isOpening c =
    c == '('
    || c == '['
    || c == '{'
    || c == '<'

isClosing :: Char -> Bool
isClosing c =
    c == ')'
    || c == ']'
    || c == '}'
    ||c == '>'

-- Get points to corrupted bracket
corrupted :: Char -> Int
corrupted x = findWithDefault 0 x mapPoints

-- Check wether brackets are matching
isMatching :: Char -> Char -> Bool
isMatching x y = findWithDefault 'x' x mapBrackets == y

-- Read an expression and determine the corruption points, 
-- aswell as the not matched brackets
readInput :: String -> String -> (String, Int)
readInput as [] = (as, 0)
readInput [] (x:xs)
    | isOpening x = readInput [x] xs
    | otherwise = ([], corrupted x)
readInput (a:as) (x:xs)
  | isOpening x = readInput (x:(a:as)) xs
  | isClosing x && isMatching a x = readInput as xs
  | otherwise = ([], corrupted x)

-- Calculate points of all corrupted expressions
calcPoints :: [String] -> Int
calcPoints = foldr ((+) . snd . readInput []) 0

-- Calculate the task2 points for the missing brackets in expression
calc :: String -> Int -> Int
calc xs a
  = foldl
      (\ a x -> (5 * a) + findWithDefault 0 x mapPointsTask2) a xs

-- Filter out all corrupted expressions
notCorrupted :: [String] -> [String]
notCorrupted xs = filter (/="") $ map (fst . ([] `readInput`)) xs

-- Get all remaining brackets from non corrupted expressions
getRemaining :: [String] -> [String]
getRemaining xs = map (map (\ x -> findWithDefault 'x' x mapBrackets)) $ notCorrupted xs

-- Get the middle value of points
getMiddle :: [String] -> Int
getMiddle xs = 
    let ys = getRemaining xs in
    let zs = sort (map (`calc` 0) ys) in
        zs !! (length zs `div` 2)

main :: IO()
main = do
    contents <- readFile "inputs\\Day10.txt"
    let input = lines contents
    print $ calcPoints input
    print $ getMiddle input