module Aoc.Y2021.ParseExample where

import Text.Parsec
import Text.Parsec.Text
import GHC.Natural
import Control.Monad
import Data.Text (pack)


data Month = Month
    { theYear  :: Natural
    , theMonth :: Natural
    }
    deriving Show

yearP :: Parser Natural
yearP = read <$> count 4 digit

monthP :: Parser Natural
monthP = read <$> count 2 digit

dash :: Parser ()
dash = void (char '-')

yearFirstP :: Parser Month
yearFirstP =
  do
    y <- yearP
    _ <- dash
    m <- monthP
    return (Month y m)

monthFirstP :: Parser Month
monthFirstP =
  do
    m <- monthP
    _ <- dash
    y <- yearP
    return (Month y m)

-- SIMPLE EXAMPLE
data Expr = Add Integer Integer
  deriving (Show, Read)

intP :: Read a => Parser a
intP = do
  x <- count 1 digit
  return (read x)

add :: Parser ()
add = void (char '+')

simpleP :: Parser Expr
simpleP = do
  x <- intP
  _ <- add
  y <- intP
  return (Add x y)

-- MORE COMPLEX EXAMPLE
data Tree = Inner Tree Tree | Leaf String
  deriving (Show)

leafP :: Parser Tree
leafP = do
  x <- many1 letter <|> count 1 digit
  return (Leaf x)

pipeP :: Parser ()
pipeP = void (char '|')

lastInnerP :: Parser Tree
lastInnerP = do
  x <- leafP
  _ <- pipeP
  y <- leafP
  return (Inner x y)

innerP :: Parser Tree
innerP = do
  x <- lastInnerP
  _ <- char '#'
  y <- lastInnerP
  return (Inner x y)

treeP :: Parser Tree
treeP = do
  x <- innerP
  _ <- space
  y <- innerP
  return (Inner x y)

-- SIMPLE BRACKETS
data Bracket = Enclosing Bracket Bracket | NextTo Bracket Bracket | Round Char Char
  deriving (Show)

opening :: Parser Char
opening = do
  char '('

closing :: Parser Char
closing = do
  char ')'

roundP :: Parser Bracket
roundP = do
  x <- opening
  y <- closing
  return (Round x y)

encP :: Parser Bracket
encP = do
  x <- opening
  y <- recEncP
  z <- closing
  return (Enclosing (Round x z) y)

recEncP :: Parser Bracket
recEncP = do
  -- Problem is, that roundP can consume something and then fail, 
  -- therefore we need "try" for backtracking.
  try roundP <|> encP

bracketP :: Parser Bracket
bracketP = do
  x <- recEncP 
  y <- try bracketP <|> recEncP
  return (NextTo x y)

main :: IO ()
main = do
    print $ parse yearFirstP "" (pack "2021-10")
    print $ parse monthFirstP "" (pack "10-2021")
    --
    print $ parse simpleP "" (pack "1+1")
    --
    print $ parse leafP "" (pack "a")
    print $ parse leafP "" (pack "1")
    print $ parse lastInnerP "" (pack "a|b")
    print $ parse lastInnerP "" (pack "ab|cd")
    print $ parse innerP "" (pack "a|b#c|d")
    print $ parse treeP "" (pack "a|b#c|d e|f#g|h")
    --
    print $ parse recEncP "" (pack "()")
    print $ parse recEncP "" (pack "(())")
    print $ parse recEncP "" (pack "((()))")
    print $ parse bracketP "" (pack "()()")
    print $ parse bracketP "" (pack "(())()")
    print $ parse bracketP "" (pack "(())()()")