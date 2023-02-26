module Main where

import Data.Char (toUpper)
import System.IO

removePunctuation :: String -> String
removePunctuation = filter (`notElem` ".,?!-_:;/()'\"")

makeUppercase :: String -> String
makeUppercase = map toUpper

removeUnder3Letters :: String -> String
removeUnder3Letters = unwords . filter (\w -> length w > 3) . words

main :: IO ()
main = do
  putStr "Introduce numele fisierului pentru a fi procesat: "
  hFlush stdout
  filePath <- getLine
  contents <- readFile filePath
  putStr (removeUnder3Letters $ makeUppercase $ removePunctuation contents)
