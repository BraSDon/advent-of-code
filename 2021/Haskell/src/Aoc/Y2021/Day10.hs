module Aoc.Y2021.Day10 where

import Text.Parsec
import Text.Parsec.Text
import GHC.Natural
import Control.Monad
import Data.Text (pack)

data Bracket = Enclosing Bracket Bracket | NextTo Bracket Bracket | Bracket Char Char
    deriving (Show)

-- Round Bracket
oRound :: Parser Char
oRound = do char '('

cRound :: Parser Char
cRound = do char ')'

roundP :: Parser Bracket
roundP = do
  x <- oRound
  y <- cRound
  return (Bracket x y)

-- Square bracket
oSquare :: Parser Char
oSquare = do char '['

cSquare :: Parser Char
cSquare = do char ']'

squareP :: Parser Bracket
squareP = do
    x <- oSquare
    y <- cSquare
    return (Bracket x y)

-- Curly bracket
oCurly :: Parser Char
oCurly = do char '{'

cCurly :: Parser Char
cCurly = do char '}'

curlyP :: Parser Bracket
curlyP = do
    x <- oCurly
    y <- cCurly
    return (Bracket x y)

-- Arrow bracket
oArrow :: Parser Char 
oArrow = do char '<'

cArrow :: Parser Char 
cArrow = do char '>'

arrowP :: Parser Bracket
arrowP = do
    x <- oArrow
    y <- cArrow
    return (Bracket x y)

-- Parser for enclosing brackets
specialEncP :: Parser Char -> Parser Char -> Parser Bracket
specialEncP o c = do
  x <- o
  y <- recEncP
  z <- c
  return (Enclosing (Bracket x z) y)

-- Parser for the enclosing brackets of available bracket types
encP :: Parser Bracket
encP = do
    specialEncP oRound cRound 
    <|> specialEncP oSquare cSquare 
    <|> specialEncP oCurly cCurly
    <|> specialEncP oArrow cArrow

-- Parser for available bracket types
endP :: Parser Bracket
endP = do
    roundP 
    <|> squareP 
    <|> curlyP 
    <|> arrowP

recEncP :: Parser Bracket
recEncP = do
  -- Problem is, that roundP can consume something and then fail, 
  -- therefore we need "try" for backtracking.
  try endP <|> encP

nextToP :: Parser Bracket
nextToP = do
  x <- recEncP
  y <- try nextToP <|> recEncP
  return (NextTo x y)

bracketP :: Parser Bracket
bracketP = do
    try nextToP <|> recEncP

main :: IO()
main = do
    print $ parse bracketP "" (pack "()")
    print $ parse bracketP "" (pack "(())")
    print $ parse bracketP "" (pack "()()")
    print $ parse bracketP "" (pack "(())()")

    print $ parse bracketP "" (pack "{}")
    print $ parse bracketP "" (pack "[]")
    print $ parse bracketP "" (pack "<>")

    print $ parse bracketP "" (pack "({})")
    print $ parse bracketP "" (pack "[{<()>}]")
    -- This does not work yet. Problem is, that I need to allow nextTo in the recursive case.
    print $ parse bracketP "" (pack "{([(<{}[<>]>)])}")
    -- They are all supposed to fail
    print $ parse bracketP "" (pack "{([(<{}[<>[]}>{[]{[(<()>")
    print $ parse bracketP "" (pack  "[[<[([]))<([[{}[[()]]]")
    print $ parse bracketP "" (pack "[{[{({}]{}}([{[{{{}}([]")
    print $ parse bracketP "" (pack "[<(<(<(<{}))><([]([]()")
    print $ parse bracketP "" (pack "<{([([[(<>()){}]>(<<{{")