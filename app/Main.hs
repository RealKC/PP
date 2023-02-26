module Main where

import System.IO

main :: IO ()
main = do
  putStr "Introduce numele fisierului pentru a fi procesat: "
  hFlush stdout
  filePath <- getLine
  contents <- readFile filePath
  putStr contents
