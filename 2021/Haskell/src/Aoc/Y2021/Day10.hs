module Aoc.Y2021.Day10 where

import Text.Parsec
import Text.Parsec.Text
import GHC.Natural
import Control.Monad
import Data.Text (pack)

data Bracket = Enclosing Bracket Bracket |
    Round Char Char | Square Char Char | Curly Char Char | Angle Char Char
    deriving (Show)

-- Find some way to implement recursive parsing.
-- So if "({" then first parse "(" as start of round bracket, then parse "{" as Enclosing Round Curly



