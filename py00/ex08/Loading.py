import os

BLOCKS = [
    "\u258F",  # 1/8
    "\u258E",  # 2/8
    "\u258D",  # 3/8
    "\u258C",  # 4/8
    "\u258B",  # 5/8
    "\u258A",  # 6/8
    "\u2589",  # 7/8
    "\u2588",  # 8/8 (full)
]

# Main sentinel.
if __name__ == "__main__":
    raise Exception(
        "ft_filter: cannot be used as main."
    )


def _sliver_to_block(sliver: float) -> str:
    sliver = max(0.0, min(sliver, 1.0))
    idx = int(sliver * len(BLOCKS))
    if idx == len(BLOCKS):
        idx -= 1
    return BLOCKS[idx]


def _render_bar(mid_len: int, int_indx: int, sliver: float) -> str:
    bar = []

    # full blocks
    bar.extend(["\u2588"] * int_indx)

    # fractional block
    if int_indx < mid_len:
        bar.append(_sliver_to_block(sliver))

    # padding
    bar.extend([" "] * (mid_len - len(bar)))

    return "".join(bar)


def ft_tqdm(lst: range):
    os.system("")  # fix Windows ANSI

    lst_len = len(lst)
    progress = 0

    # layout pieces
    # front shows: " XX%|"
    # back shows: "|  12/100"
    terminal_width = os.get_terminal_size().columns

    back = (" | {cur:>3}/{total}" + (" " * 18)).format(cur=0, total=lst_len)
    back_len = len(back)

    # mid length = width minus front and back
    mid_len = terminal_width - back_len - 8   # 8 chars for " 100% |"
    if mid_len < 10:
        mid_len = 10

    # initial print (empty; cursor moves up to overwrite)
    print(" " * terminal_width, end="\033[1A\033[?25l")

    for i in lst:
        progress += 1
        prog_percent = progress / lst_len
        indx = prog_percent * mid_len
        int_indx = int(indx)
        sliver = indx - int_indx

        # construct parts
        percent = f"{int(prog_percent*100):3d}%|"
        bar = _render_bar(mid_len - 1, int_indx, sliver)
        back = f"| {progress:>3}/{lst_len}"

        yield

        # move to beginning and rewrite full line
        print(f"\033[1G{percent}{bar}{back}", end="", flush=True)

    print("\033[?25h", end="")  # show cursor again
