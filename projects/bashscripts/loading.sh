#!/usr/bin/env bash
# 4x4 Braille loading animation (two 2x4 cells side-by-side)
# A single "blank" dot walks around the perimeter.

set -euo pipefail
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Map (x_in_cell = 1..2, y = 1..4) -> braille dot index (1..8)
dot_index() {
  local x=$1 y=$2
  if [[ "$x" -eq 1 ]]; then
    case "$y" in
      1) echo 1 ;;
      2) echo 2 ;;
      3) echo 3 ;;
      4) echo 7 ;;
    esac
  else # x == 2
    case "$y" in
      1) echo 4 ;;
      2) echo 5 ;;
      3) echo 6 ;;
      4) echo 8 ;;
    esac
  fi
}

# Print a single braille char with ONE dot turned off for the given cell.
# cell: "L" or "R"
# blank_x, blank_y: global 4x4 coords (1..4, 1..4)
cell_char_with_blank() {
  local cell="$1" blank_x="$2" blank_y="$3"
  local FULL=0x28FF
  local base=$FULL

  if [[ "$cell" == "L" && "$blank_x" -le 2 ]]; then
    local x_in_cell="$blank_x"
    local y="$blank_y"
    local idx; idx=$(dot_index "$x_in_cell" "$y")
    local mask=$((1 << (idx - 1)))
    base=$(( FULL - mask ))
  elif [[ "$cell" == "R" && "$blank_x" -ge 3 ]]; then
    local x_in_cell=$((blank_x - 2))
    local y="$blank_y"
    local idx; idx=$(dot_index "$x_in_cell" "$y")
    local mask=$((1 << (idx - 1)))
    base=$(( FULL - mask ))
  fi

  # Build a \UXXXXXXXX escape first, then print it with %b (interprets escapes)
  local esc
  printf -v esc '\\U%08X' "$base"
  printf "%b" "$esc"
}

# Build the 4x4 perimeter path: top row → right col → bottom row → left col
build_perimeter() {
  local -n OUT=$1
  OUT=()
  for x in 1 2 3 4; do OUT+=("$x,1"); done      # top
  for y in 2 3; do OUT+=("4,$y"); done          # right (inner)
  for x in 4 3 2 1; do OUT+=("$x,4"); done      # bottom
  for y in 3 2; do OUT+=("1,$y"); done          # left (inner)
}

cleanup() { tput cnorm 2>/dev/null || true; echo; }
trap cleanup EXIT

tput civis 2>/dev/null || true

declare -a PERIM
build_perimeter PERIM

i=0
while true; do
  IFS=',' read -r bx by <<< "${PERIM[i]}"

  left=$(cell_char_with_blank "L" "$bx" "$by")
  right=$(cell_char_with_blank "R" "$bx" "$by")

  printf "\r%s%s  Loading..." "$left" "$right"
  sleep 0.08

  i=$(( (i + 1) % ${#PERIM[@]} ))
done
