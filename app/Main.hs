module Main where

import Data.Char (toUpper)
import System.IO

removePunctuation :: String -> String
removePunctuation = filter (`notElem` ".,?!-_:;/()'\"")

makeUppercase :: String -> String
makeUppercase = map toUpper

main :: IO ()
main = do
  putStr "Introduce numele fisierului pentru a fi procesat: "
  hFlush stdout
  filePath <- getLine
  contents <- readFile filePath
  putStr (makeUppercase $ removePunctuation contents)
