# lk_religion

Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.

Each analysis now lives in its own folder under [`analyses/`](analyses/), together with its own README, workflow script, and related data files. The sections below are copied from those child READMEs.

- [`analyses/a1_national_totals/`](analyses/a1_national_totals/)
- [`analyses/a2_by_district/`](analyses/a2_by_district/)
- [`analyses/a3_proportion_change/`](analyses/a3_proportion_change/)
- [`analyses/a4_by_dsd/`](analyses/a4_by_dsd/)
- [`analyses/a5_proportion_change_by_dsd/`](analyses/a5_proportion_change_by_dsd/)

---

## A1. National Population by Religion

![A1 representative chart](analyses/a1_national_totals/chart.png)

| Religion | 2012 | 2024 | Change | Annual Growth | % of Population |
|---|---:|---:|---:|---:|---:|
| Buddhist | 14,271,183 | 15,199,093 | <span style="color:green">▲</span> +927,910 | <span style="color:green">▲</span> +0.53% | 69.8% |
| Hindu | 2,561,142 | 2,734,839 | <span style="color:green">▲</span> +173,697 | <span style="color:green">▲</span> +0.55% | 12.6% |
| Islam | 1,967,008 | 2,337,379 | <span style="color:green">▲</span> +370,371 | <span style="color:green">▲</span> +1.45% | 10.7% |
| RomanCatholic | 1,261,136 | 1,224,348 | <span style="color:red">▼</span> -36,788 | <span style="color:red">▼</span> -0.25% | 5.6% |
| OtherChristian | 290,920 | 282,185 | <span style="color:red">▼</span> -8,735 | <span style="color:red">▼</span> -0.25% | 1.3% |
| Other | 6,387 | 3,956 | <span style="color:red">▼</span> -2,431 | <span style="color:red">▼</span> -3.91% | 0.0% |
| **Total** | **20,357,776** | **21,781,800** | **<span style="color:green">▲</span> +1,424,024** | **<span style="color:green">▲</span> +0.57%** |

### Commentary

- Sri Lanka's total population grew from **20,357,776** (2012) to **21,781,800** (2024), an increase of **+1,424,024** at an annual rate of **+0.57%**.
- **Buddhism** remains the dominant religion, accounting for **69.8%** of the population in 2024, growing at **+0.53%** per year.
- **Islam** has the fastest growth rate among major religions at **+1.45%** per year, reaching a share of **10.7%** in 2024.
- **Roman Catholic** and **Other Christian** communities show slight declines over the period.

---

## A2. Religion by District: Key Trends

![A2 district change maps](analyses/a2_by_district/chart.png)

District-level **% change in population** for each religion between 2012 and 2024. Districts are shaded from **red (decline)** to **green (growth)**.

### Buddhist

| District | 2012 | 2024 | Change | % Change | % of Natl |
|---|---:|---:|---:|---:|---:|
| Jaffna | 2,168 | 2,788 | <span style="color:green">▲</span> +620 | <span style="color:green">▲</span> +28.6% | 0.0% |
| Mullaitivu | 8,140 | 10,293 | <span style="color:green">▲</span> +2,153 | <span style="color:green">▲</span> +26.4% | 0.1% |
| Kilinochchi | 1,275 | 1,533 | <span style="color:green">▲</span> +258 | <span style="color:green">▲</span> +20.2% | 0.0% |
| Monaragala | 426,762 | 498,436 | <span style="color:green">▲</span> +71,674 | <span style="color:green">▲</span> +16.8% | 3.3% |
| Hambantota | 580,344 | 649,736 | <span style="color:green">▲</span> +69,392 | <span style="color:green">▲</span> +12.0% | 4.3% |
| Anuradhapura | 775,366 | 862,807 | <span style="color:green">▲</span> +87,441 | <span style="color:green">▲</span> +11.3% | 5.7% |
| Ampara | 251,427 | 276,176 | <span style="color:green">▲</span> +24,749 | <span style="color:green">▲</span> +9.8% | 1.8% |
| Polonnaruwa | 364,229 | 399,488 | <span style="color:green">▲</span> +35,259 | <span style="color:green">▲</span> +9.7% | 2.6% |
| Puttalam | 329,705 | 361,148 | <span style="color:green">▲</span> +31,443 | <span style="color:green">▲</span> +9.5% | 2.4% |
| Vavuniya | 16,799 | 18,292 | <span style="color:green">▲</span> +1,493 | <span style="color:green">▲</span> +8.9% | 0.1% |
| Kurunegala | 1,430,958 | 1,557,554 | <span style="color:green">▲</span> +126,596 | <span style="color:green">▲</span> +8.8% | 10.2% |
| Matale | 385,151 | 418,608 | <span style="color:green">▲</span> +33,457 | <span style="color:green">▲</span> +8.7% | 2.8% |
| Badulla | 591,799 | 636,988 | <span style="color:green">▲</span> +45,189 | <span style="color:green">▲</span> +7.6% | 4.2% |
| Trincomalee | 99,344 | 106,919 | <span style="color:green">▲</span> +7,575 | <span style="color:green">▲</span> +7.6% | 0.7% |
| Gampaha | 1,642,767 | 1,744,475 | <span style="color:green">▲</span> +101,708 | <span style="color:green">▲</span> +6.2% | 11.5% |
| Kalutara | 1,018,909 | 1,080,638 | <span style="color:green">▲</span> +61,729 | <span style="color:green">▲</span> +6.1% | 7.1% |
| Ratnapura | 943,464 | 999,682 | <span style="color:green">▲</span> +56,218 | <span style="color:green">▲</span> +6.0% | 6.6% |
| Kandy | 1,009,220 | 1,063,511 | <span style="color:green">▲</span> +54,291 | <span style="color:green">▲</span> +5.4% | 7.0% |
| Colombo | 1,632,125 | 1,682,524 | <span style="color:green">▲</span> +50,399 | <span style="color:green">▲</span> +3.1% | 11.1% |
| Galle | 998,647 | 1,026,031 | <span style="color:green">▲</span> +27,384 | <span style="color:green">▲</span> +2.7% | 6.8% |
| Matara | 766,323 | 787,303 | <span style="color:green">▲</span> +20,980 | <span style="color:green">▲</span> +2.7% | 5.2% |
| Kegalle | 709,917 | 728,929 | <span style="color:green">▲</span> +19,012 | <span style="color:green">▲</span> +2.7% | 4.8% |
| Nuwara Eliya | 278,254 | 278,828 | <span style="color:green">▲</span> +574 | <span style="color:green">▲</span> +0.2% | 1.8% |
| Batticaloa | 6,281 | 6,024 | <span style="color:red">▼</span> -257 | <span style="color:red">▼</span> -4.1% | 0.0% |
| Mannar | 1,809 | 382 | <span style="color:red">▼</span> -1,427 | <span style="color:red">▼</span> -78.9% | 0.0% |

***Jaffna** grew fastest at **+28.6%**. **Mannar** saw the steepest decline at **-78.9%**. **Kurunegala** had the largest absolute increase (**+126,596**).*

### Hindu

| District | 2012 | 2024 | Change | % Change | % of Natl |
|---|---:|---:|---:|---:|---:|
| Gampaha | 52,973 | 69,429 | <span style="color:green">▲</span> +16,456 | <span style="color:green">▲</span> +31.1% | 2.5% |
| Mullaitivu | 69,377 | 88,738 | <span style="color:green">▲</span> +19,361 | <span style="color:green">▲</span> +27.9% | 3.2% |
| Monaragala | 11,997 | 14,974 | <span style="color:green">▲</span> +2,977 | <span style="color:green">▲</span> +24.8% | 0.5% |
| Kurunegala | 14,716 | 17,487 | <span style="color:green">▲</span> +2,771 | <span style="color:green">▲</span> +18.8% | 0.6% |
| Kilinochchi | 92,986 | 110,258 | <span style="color:green">▲</span> +17,272 | <span style="color:green">▲</span> +18.6% | 4.0% |
| Anuradhapura | 3,231 | 3,755 | <span style="color:green">▲</span> +524 | <span style="color:green">▲</span> +16.2% | 0.1% |
| Hambantota | 1,222 | 1,401 | <span style="color:green">▲</span> +179 | <span style="color:green">▲</span> +14.6% | 0.1% |
| Ampara | 102,829 | 114,586 | <span style="color:green">▲</span> +11,757 | <span style="color:green">▲</span> +11.4% | 4.2% |
| Batticaloa | 338,882 | 374,836 | <span style="color:green">▲</span> +35,954 | <span style="color:green">▲</span> +10.6% | 13.7% |
| Trincomalee | 98,442 | 108,050 | <span style="color:green">▲</span> +9,608 | <span style="color:green">▲</span> +9.8% | 4.0% |
| Mannar | 24,027 | 26,214 | <span style="color:green">▲</span> +2,187 | <span style="color:green">▲</span> +9.1% | 1.0% |
| Kandy | 133,744 | 144,618 | <span style="color:green">▲</span> +10,874 | <span style="color:green">▲</span> +8.1% | 5.3% |
| Kalutara | 39,541 | 42,528 | <span style="color:green">▲</span> +2,987 | <span style="color:green">▲</span> +7.6% | 1.6% |
| Matale | 43,432 | 46,181 | <span style="color:green">▲</span> +2,749 | <span style="color:green">▲</span> +6.3% | 1.7% |
| Colombo | 186,303 | 197,759 | <span style="color:green">▲</span> +11,456 | <span style="color:green">▲</span> +6.1% | 7.2% |
| Badulla | 157,608 | 166,380 | <span style="color:green">▲</span> +8,772 | <span style="color:green">▲</span> +5.6% | 6.1% |
| Polonnaruwa | 6,886 | 7,215 | <span style="color:green">▲</span> +329 | <span style="color:green">▲</span> +4.8% | 0.3% |
| Nuwara Eliya | 363,163 | 377,266 | <span style="color:green">▲</span> +14,103 | <span style="color:green">▲</span> +3.9% | 13.8% |
| Kegalle | 54,350 | 56,199 | <span style="color:green">▲</span> +1,849 | <span style="color:green">▲</span> +3.4% | 2.1% |
| Ratnapura | 101,962 | 103,883 | <span style="color:green">▲</span> +1,921 | <span style="color:green">▲</span> +1.9% | 3.8% |
| Jaffna | 483,255 | 489,521 | <span style="color:green">▲</span> +6,266 | <span style="color:green">▲</span> +1.3% | 17.9% |
| Galle | 15,584 | 15,600 | <span style="color:green">▲</span> +16 | <span style="color:green">▲</span> +0.1% | 0.6% |
| Puttalam | 28,811 | 28,832 | <span style="color:green">▲</span> +21 | <span style="color:green">▲</span> +0.1% | 1.1% |
| Vavuniya | 119,400 | 114,504 | <span style="color:red">▼</span> -4,896 | <span style="color:red">▼</span> -4.1% | 4.2% |
| Matara | 16,421 | 14,625 | <span style="color:red">▼</span> -1,796 | <span style="color:red">▼</span> -10.9% | 0.5% |

***Gampaha** grew fastest at **+31.1%**. **Matara** saw the steepest decline at **-10.9%**. **Batticaloa** had the largest absolute increase (**+35,954**).*

### Islam

| District | 2012 | 2024 | Change | % Change | % of Natl |
|---|---:|---:|---:|---:|---:|
| Mannar | 16,512 | 33,883 | <span style="color:green">▲</span> +17,371 | <span style="color:green">▲</span> +105.2% | 1.4% |
| Kilinochchi | 700 | 1,394 | <span style="color:green">▲</span> +694 | <span style="color:green">▲</span> +99.1% | 0.1% |
| Jaffna | 2,363 | 4,352 | <span style="color:green">▲</span> +1,989 | <span style="color:green">▲</span> +84.2% | 0.2% |
| Mullaitivu | 1,880 | 3,279 | <span style="color:green">▲</span> +1,399 | <span style="color:green">▲</span> +74.4% | 0.1% |
| Vavuniya | 11,972 | 17,775 | <span style="color:green">▲</span> +5,803 | <span style="color:green">▲</span> +48.5% | 0.8% |
| Trincomalee | 159,418 | 205,664 | <span style="color:green">▲</span> +46,246 | <span style="color:green">▲</span> +29.0% | 8.8% |
| Monaragala | 9,809 | 12,262 | <span style="color:green">▲</span> +2,453 | <span style="color:green">▲</span> +25.0% | 0.5% |
| Polonnaruwa | 30,465 | 37,097 | <span style="color:green">▲</span> +6,632 | <span style="color:green">▲</span> +21.8% | 1.6% |
| Kurunegala | 117,810 | 143,299 | <span style="color:green">▲</span> +25,489 | <span style="color:green">▲</span> +21.6% | 6.1% |
| Kalutara | 114,556 | 138,230 | <span style="color:green">▲</span> +23,674 | <span style="color:green">▲</span> +20.7% | 5.9% |
| Ampara | 281,987 | 339,896 | <span style="color:green">▲</span> +57,909 | <span style="color:green">▲</span> +20.5% | 14.5% |
| Batticaloa | 134,065 | 161,494 | <span style="color:green">▲</span> +27,429 | <span style="color:green">▲</span> +20.5% | 6.9% |
| Gampaha | 112,746 | 134,422 | <span style="color:green">▲</span> +21,676 | <span style="color:green">▲</span> +19.2% | 5.8% |
| Kegalle | 61,164 | 72,616 | <span style="color:green">▲</span> +11,452 | <span style="color:green">▲</span> +18.7% | 3.1% |
| Hambantota | 15,204 | 17,947 | <span style="color:green">▲</span> +2,743 | <span style="color:green">▲</span> +18.0% | 0.8% |
| Puttalam | 150,404 | 176,963 | <span style="color:green">▲</span> +26,559 | <span style="color:green">▲</span> +17.7% | 7.6% |
| Anuradhapura | 71,493 | 83,979 | <span style="color:green">▲</span> +12,486 | <span style="color:green">▲</span> +17.5% | 3.6% |
| Galle | 39,267 | 46,038 | <span style="color:green">▲</span> +6,771 | <span style="color:green">▲</span> +17.2% | 2.0% |
| Matara | 25,614 | 29,858 | <span style="color:green">▲</span> +4,244 | <span style="color:green">▲</span> +16.6% | 1.3% |
| Matale | 45,682 | 52,224 | <span style="color:green">▲</span> +6,542 | <span style="color:green">▲</span> +14.3% | 2.2% |
| Kandy | 197,076 | 223,997 | <span style="color:green">▲</span> +26,921 | <span style="color:green">▲</span> +13.7% | 9.6% |
| Badulla | 47,192 | 53,563 | <span style="color:green">▲</span> +6,371 | <span style="color:green">▲</span> +13.5% | 2.3% |
| Ratnapura | 24,446 | 26,796 | <span style="color:green">▲</span> +2,350 | <span style="color:green">▲</span> +9.6% | 1.1% |
| Colombo | 274,067 | 298,422 | <span style="color:green">▲</span> +24,355 | <span style="color:green">▲</span> +8.9% | 12.8% |
| Nuwara Eliya | 21,116 | 21,929 | <span style="color:green">▲</span> +813 | <span style="color:green">▲</span> +3.9% | 0.9% |

***Mannar** grew fastest at **+105.2%**. **Nuwara Eliya** had the slowest growth at **+3.9%**. **Ampara** had the largest absolute increase (**+57,909**).*

### Roman Catholic

| District | 2012 | 2024 | Change | % Change | % of Natl |
|---|---:|---:|---:|---:|---:|
| Mullaitivu | 9,063 | 13,982 | <span style="color:green">▲</span> +4,919 | <span style="color:green">▲</span> +54.3% | 1.1% |
| Kilinochchi | 12,063 | 14,446 | <span style="color:green">▲</span> +2,383 | <span style="color:green">▲</span> +19.8% | 1.2% |
| Mannar | 52,415 | 57,713 | <span style="color:green">▲</span> +5,298 | <span style="color:green">▲</span> +10.1% | 4.7% |
| Batticaloa | 24,454 | 25,803 | <span style="color:green">▲</span> +1,349 | <span style="color:green">▲</span> +5.5% | 2.1% |
| Jaffna | 75,474 | 77,197 | <span style="color:green">▲</span> +1,723 | <span style="color:green">▲</span> +2.3% | 6.3% |
| Matara | 2,432 | 2,445 | <span style="color:green">▲</span> +13 | <span style="color:green">▲</span> +0.5% | 0.2% |
| Puttalam | 240,221 | 240,975 | <span style="color:green">▲</span> +754 | <span style="color:green">▲</span> +0.3% | 19.7% |
| Trincomalee | 14,493 | 14,353 | <span style="color:red">▼</span> -140 | <span style="color:red">▼</span> -1.0% | 1.2% |
| Matale | 7,899 | 7,797 | <span style="color:red">▼</span> -102 | <span style="color:red">▼</span> -1.3% | 0.6% |
| Gampaha | 449,398 | 442,291 | <span style="color:red">▼</span> -7,107 | <span style="color:red">▼</span> -1.6% | 36.1% |
| Ampara | 7,588 | 7,351 | <span style="color:red">▼</span> -237 | <span style="color:red">▼</span> -3.1% | 0.6% |
| Galle | 4,415 | 4,207 | <span style="color:red">▼</span> -208 | <span style="color:red">▼</span> -4.7% | 0.3% |
| Nuwara Eliya | 33,476 | 31,705 | <span style="color:red">▼</span> -1,771 | <span style="color:red">▼</span> -5.3% | 2.6% |
| Kurunegala | 43,707 | 40,273 | <span style="color:red">▼</span> -3,434 | <span style="color:red">▼</span> -7.9% | 3.3% |
| Kalutara | 39,774 | 36,510 | <span style="color:red">▼</span> -3,264 | <span style="color:red">▼</span> -8.2% | 3.0% |
| Hambantota | 1,139 | 1,017 | <span style="color:red">▼</span> -122 | <span style="color:red">▼</span> -10.7% | 0.1% |
| Colombo | 162,260 | 139,882 | <span style="color:red">▼</span> -22,378 | <span style="color:red">▼</span> -13.8% | 11.4% |
| Anuradhapura | 6,747 | 5,760 | <span style="color:red">▼</span> -987 | <span style="color:red">▼</span> -14.6% | 0.5% |
| Vavuniya | 15,305 | 12,785 | <span style="color:red">▼</span> -2,520 | <span style="color:red">▼</span> -16.5% | 1.0% |
| Kandy | 22,379 | 18,623 | <span style="color:red">▼</span> -3,756 | <span style="color:red">▼</span> -16.8% | 1.5% |
| Kegalle | 8,777 | 7,292 | <span style="color:red">▼</span> -1,485 | <span style="color:red">▼</span> -16.9% | 0.6% |
| Polonnaruwa | 3,192 | 2,560 | <span style="color:red">▼</span> -632 | <span style="color:red">▼</span> -19.8% | 0.2% |
| Badulla | 12,020 | 9,593 | <span style="color:red">▼</span> -2,427 | <span style="color:red">▼</span> -20.2% | 0.8% |
| Ratnapura | 10,844 | 8,607 | <span style="color:red">▼</span> -2,237 | <span style="color:red">▼</span> -20.6% | 0.7% |
| Monaragala | 1,601 | 1,181 | <span style="color:red">▼</span> -420 | <span style="color:red">▼</span> -26.2% | 0.1% |

***Mullaitivu** grew fastest at **+54.3%**. **Monaragala** saw the steepest decline at **-26.2%**. **Mannar** had the largest absolute increase (**+5,298**).*

### Other Christian

| District | 2012 | 2024 | Change | % Change | % of Natl |
|---|---:|---:|---:|---:|---:|
| Mullaitivu | 3,664 | 6,315 | <span style="color:green">▲</span> +2,651 | <span style="color:green">▲</span> +72.4% | 2.2% |
| Kilinochchi | 6,436 | 9,074 | <span style="color:green">▲</span> +2,638 | <span style="color:green">▲</span> +41.0% | 3.2% |
| Batticaloa | 22,833 | 27,728 | <span style="color:green">▲</span> +4,895 | <span style="color:green">▲</span> +21.4% | 9.8% |
| Ampara | 5,541 | 6,486 | <span style="color:green">▲</span> +945 | <span style="color:green">▲</span> +17.1% | 2.3% |
| Mannar | 4,790 | 5,560 | <span style="color:green">▲</span> +770 | <span style="color:green">▲</span> +16.1% | 2.0% |
| Matara | 3,208 | 3,619 | <span style="color:green">▲</span> +411 | <span style="color:green">▲</span> +12.8% | 1.3% |
| Vavuniya | 8,498 | 8,895 | <span style="color:green">▲</span> +397 | <span style="color:green">▲</span> +4.7% | 3.2% |
| Jaffna | 20,511 | 20,857 | <span style="color:green">▲</span> +346 | <span style="color:green">▲</span> +1.7% | 7.4% |
| Galle | 5,315 | 5,377 | <span style="color:green">▲</span> +62 | <span style="color:green">▲</span> +1.2% | 1.9% |
| Anuradhapura | 3,660 | 3,656 | <span style="color:red">▼</span> -4 | <span style="color:red">▼</span> -0.1% | 1.3% |
| Nuwara Eliya | 15,508 | 15,474 | <span style="color:red">▼</span> -34 | <span style="color:red">▼</span> -0.2% | 5.5% |
| Trincomalee | 7,774 | 7,714 | <span style="color:red">▼</span> -60 | <span style="color:red">▼</span> -0.8% | 2.7% |
| Gampaha | 46,080 | 44,540 | <span style="color:red">▼</span> -1,540 | <span style="color:red">▼</span> -3.3% | 15.8% |
| Kurunegala | 9,926 | 9,413 | <span style="color:red">▼</span> -513 | <span style="color:red">▼</span> -5.2% | 3.3% |
| Ratnapura | 7,212 | 6,394 | <span style="color:red">▼</span> -818 | <span style="color:red">▼</span> -11.3% | 2.3% |
| Puttalam | 12,093 | 10,619 | <span style="color:red">▼</span> -1,474 | <span style="color:red">▼</span> -12.2% | 3.8% |
| Badulla | 6,615 | 5,729 | <span style="color:red">▼</span> -886 | <span style="color:red">▼</span> -13.4% | 2.0% |
| Matale | 2,342 | 2,026 | <span style="color:red">▼</span> -316 | <span style="color:red">▼</span> -13.5% | 0.7% |
| Kalutara | 8,956 | 7,733 | <span style="color:red">▼</span> -1,223 | <span style="color:red">▼</span> -13.7% | 2.7% |
| Kandy | 12,798 | 10,919 | <span style="color:red">▼</span> -1,879 | <span style="color:red">▼</span> -14.7% | 3.9% |
| Polonnaruwa | 1,276 | 1,086 | <span style="color:red">▼</span> -190 | <span style="color:red">▼</span> -14.9% | 0.4% |
| Kegalle | 6,386 | 5,387 | <span style="color:red">▼</span> -999 | <span style="color:red">▼</span> -15.6% | 1.9% |
| Colombo | 66,947 | 55,624 | <span style="color:red">▼</span> -11,323 | <span style="color:red">▼</span> -16.9% | 19.7% |
| Monaragala | 859 | 713 | <span style="color:red">▼</span> -146 | <span style="color:red">▼</span> -17.0% | 0.3% |
| Hambantota | 1,692 | 1,247 | <span style="color:red">▼</span> -445 | <span style="color:red">▼</span> -26.3% | 0.4% |

***Mullaitivu** grew fastest at **+72.4%**. **Hambantota** saw the steepest decline at **-26.3%**. **Batticaloa** had the largest absolute increase (**+4,895**).*

### Other

| District | 2012 | 2024 | Change | % Change | % of Natl |
|---|---:|---:|---:|---:|---:|
| Polonnaruwa | 40 | 84 | <span style="color:green">▲</span> +44 | <span style="color:green">▲</span> +110.0% | 2.1% |
| Ampara | 30 | 56 | <span style="color:green">▲</span> +26 | <span style="color:green">▲</span> +86.7% | 1.4% |
| Anuradhapura | 78 | 123 | <span style="color:green">▲</span> +45 | <span style="color:green">▲</span> +57.7% | 3.1% |
| Kandy | 165 | 227 | <span style="color:green">▲</span> +62 | <span style="color:green">▲</span> +37.6% | 5.7% |
| Matale | 25 | 34 | <span style="color:green">▲</span> +9 | <span style="color:green">▲</span> +36.0% | 0.9% |
| Gampaha | 869 | 985 | <span style="color:green">▲</span> +116 | <span style="color:green">▲</span> +13.3% | 24.9% |
| Galle | 106 | 119 | <span style="color:green">▲</span> +13 | <span style="color:green">▲</span> +12.3% | 3.0% |
| Kegalle | 54 | 53 | <span style="color:red">▼</span> -1 | <span style="color:red">▼</span> -1.9% | 1.3% |
| Matara | 50 | 39 | <span style="color:red">▼</span> -11 | <span style="color:red">▼</span> -22.0% | 1.0% |
| Ratnapura | 79 | 61 | <span style="color:red">▼</span> -18 | <span style="color:red">▼</span> -22.8% | 1.5% |
| Kurunegala | 170 | 130 | <span style="color:red">▼</span> -40 | <span style="color:red">▼</span> -23.5% | 3.3% |
| Vavuniya | 86 | 61 | <span style="color:red">▼</span> -25 | <span style="color:red">▼</span> -29.1% | 1.5% |
| Kalutara | 212 | 145 | <span style="color:red">▼</span> -67 | <span style="color:red">▼</span> -31.6% | 3.7% |
| Trincomalee | 70 | 45 | <span style="color:red">▼</span> -25 | <span style="color:red">▼</span> -35.7% | 1.1% |
| Batticaloa | 52 | 33 | <span style="color:red">▼</span> -19 | <span style="color:red">▼</span> -36.5% | 0.8% |
| Monaragala | 30 | 19 | <span style="color:red">▼</span> -11 | <span style="color:red">▼</span> -36.7% | 0.5% |
| Nuwara Eliya | 127 | 78 | <span style="color:red">▼</span> -49 | <span style="color:red">▼</span> -38.6% | 2.0% |
| Colombo | 2,262 | 1,204 | <span style="color:red">▼</span> -1,058 | <span style="color:red">▼</span> -46.8% | 30.4% |
| Jaffna | 111 | 36 | <span style="color:red">▼</span> -75 | <span style="color:red">▼</span> -67.6% | 0.9% |
| Badulla | 171 | 54 | <span style="color:red">▼</span> -117 | <span style="color:red">▼</span> -68.4% | 1.4% |
| Puttalam | 1,162 | 279 | <span style="color:red">▼</span> -883 | <span style="color:red">▼</span> -76.0% | 7.1% |
| Mannar | 17 | 4 | <span style="color:red">▼</span> -13 | <span style="color:red">▼</span> -76.5% | 0.1% |
| Hambantota | 302 | 70 | <span style="color:red">▼</span> -232 | <span style="color:red">▼</span> -76.8% | 1.8% |
| Mullaitivu | 69 | 12 | <span style="color:red">▼</span> -57 | <span style="color:red">▼</span> -82.6% | 0.3% |
| Kilinochchi | 50 | 5 | <span style="color:red">▼</span> -45 | <span style="color:red">▼</span> -90.0% | 0.1% |

***Polonnaruwa** grew fastest at **+110.0%**. **Kilinochchi** saw the steepest decline at **-90.0%**. **Gampaha** had the largest absolute increase (**+116**).*

---

## A3. Largest Change in Religious Proportion

![A3 representative chart](analyses/a3_proportion_change/chart.png)

For each district, the religion whose share of the local population changed most between 2012 and 2024.

### By District

| District | Religion | Share 2012 | Share 2024 | Change |
|---|---|---:|---:|---:|
| Mannar | Islam | 16.6% | 27.4% | <span style="color:green">▲</span> +10.8% |
| Trincomalee | Islam | 42.0% | 46.5% | <span style="color:green">▲</span> +4.4% |
| Vavuniya | Islam | 7.0% | 10.3% | <span style="color:green">▲</span> +3.4% |
| Mullaitivu | Hindu | 75.3% | 72.4% | <span style="color:red">▼</span> -2.9% |
| Ampara | Islam | 43.4% | 45.7% | <span style="color:green">▲</span> +2.2% |
| Puttalam | RomanCatholic | 31.5% | 29.4% | <span style="color:red">▼</span> -2.1% |
| Batticaloa | Islam | 25.5% | 27.1% | <span style="color:green">▲</span> +1.6% |
| Gampaha | RomanCatholic | 19.5% | 18.2% | <span style="color:red">▼</span> -1.3% |
| Kilinochchi | Hindu | 81.9% | 80.7% | <span style="color:red">▼</span> -1.3% |
| Kalutara | Islam | 9.4% | 10.6% | <span style="color:green">▲</span> +1.2% |
| Colombo | RomanCatholic | 7.0% | 5.9% | <span style="color:red">▼</span> -1.1% |
| Kegalle | Islam | 7.3% | 8.3% | <span style="color:green">▲</span> +1.1% |
| Kandy | Islam | 14.3% | 15.3% | <span style="color:green">▲</span> +1.0% |
| Nuwara Eliya | Hindu | 51.0% | 52.0% | <span style="color:green">▲</span> +1.0% |
| Kurunegala | Islam | 7.3% | 8.1% | <span style="color:green">▲</span> +0.8% |
| Polonnaruwa | Islam | 7.5% | 8.3% | <span style="color:green">▲</span> +0.8% |
| Ratnapura | Buddhist | 86.7% | 87.3% | <span style="color:green">▲</span> +0.6% |
| Galle | Islam | 3.7% | 4.2% | <span style="color:green">▲</span> +0.5% |
| Matale | Islam | 9.4% | 9.9% | <span style="color:green">▲</span> +0.5% |
| Jaffna | Hindu | 82.8% | 82.3% | <span style="color:red">▼</span> -0.5% |
| Badulla | Buddhist | 72.6% | 73.0% | <span style="color:green">▲</span> +0.4% |
| Anuradhapura | Islam | 8.3% | 8.7% | <span style="color:green">▲</span> +0.4% |
| Matara | Islam | 3.1% | 3.6% | <span style="color:green">▲</span> +0.4% |
| Monaragala | Hindu | 2.7% | 2.8% | <span style="color:green">▲</span> +0.2% |
| Hambantota | Islam | 2.5% | 2.7% | <span style="color:green">▲</span> +0.1% |

---

## A4. DSD Boundary Changes

![A4 representative chart](analyses/a4_by_dsd/chart.png)

Districts where the number of DSDs changed between censuses are listed below. Within those districts, DSDs whose population growth deviates from the national rate (+6.99% over 2012–2024) by more than 2× are flagged as **Altered** — their apparent demographic shifts likely reflect re-demarcation rather than genuine change.

**Districts with changed DSD boundaries:**

| District | DSDs 2012 | DSDs 2024 | Δ |
|---|---:|---:|---:|
| Nuwara Eliya | 5 | 10 | <span style="color:green">▲</span> +5 |
| Galle | 19 | 22 | <span style="color:green">▲</span> +3 |
| Batticaloa | 14 | 13 | <span style="color:red">▼</span> -1 |
| Ampara | 20 | 19 | <span style="color:red">▼</span> -1 |
| Ratnapura | 17 | 18 | <span style="color:green">▲</span> +1 |

**New, Altered, and Removed DSDs:**

| Status | Code | DSD | District | Pop 2012 | Pop 2024 | Pop Change |
|---|---|---|---|---:|---:|---:|
| Removed | LK-5224 | LK-5224 | Ampara | 44,632 | — | — |
| Altered | LK-5233 | Addalaichenai | Ampara | 41,968 | 53,214 | <span style="color:green">▲</span> +26.8% |
| Altered | LK-5234 | Irakkamam | Ampara | 14,383 | 17,671 | <span style="color:green">▲</span> +22.9% |
| Altered | LK-5221 | Kalmunai | Ampara | 29,800 | 52,798 | <span style="color:green">▲</span> +77.2% |
| Altered | LK-5248 | Pottuvil | Ampara | 34,809 | 42,908 | <span style="color:green">▲</span> +23.3% |
| Removed | LK-5109 | Koralai Pattu | Batticaloa | 23,376 | — | — |
| Removed | LK-5112 | LK-5112 | Batticaloa | 75,478 | — | — |
| Altered | LK-5115 | Eravur Pattu | Batticaloa | 24,643 | 94,237 | <span style="color:green">▲</span> +282.4% |
| New | LK-5139 | Eravur Town | Batticaloa | — | 26,468 | — |
| Altered | LK-3127 | Baddegama | Galle | 75,008 | 50,956 | <span style="color:red">▼</span> -32.1% |
| Altered | LK-3136 | Hikkaduwa | Galle | 101,909 | 26,216 | <span style="color:red">▼</span> -74.3% |
| New | LK-3138 | Madampagama | Galle | — | 33,408 | — |
| New | LK-3137 | Rathgama | Galle | — | 41,456 | — |
| New | LK-3128 | Wanduramba | Galle | — | 27,702 | — |
| Altered | LK-2315 | Ambagamuwa Korale | Nuwara Eliya | 205,723 | 42,538 | <span style="color:red">▼</span> -79.3% |
| Altered | LK-2306 | Hanguranketa | Nuwara Eliya | 88,528 | 58,931 | <span style="color:red">▼</span> -33.4% |
| Altered | LK-2303 | Kothmale East | Nuwara Eliya | 101,180 | 61,742 | <span style="color:red">▼</span> -39.0% |
| Altered | LK-2312 | Nuwara Eliya | Nuwara Eliya | 212,094 | 88,332 | <span style="color:red">▼</span> -58.4% |
| Altered | LK-2309 | Walapane | Nuwara Eliya | 104,119 | 65,287 | <span style="color:red">▼</span> -37.3% |
| New | LK-2304 | Kothmale West | Nuwara Eliya | — | 41,955 | — |
| New | LK-2307 | Mathurata | Nuwara Eliya | — | 33,175 | — |
| New | LK-2310 | Nildandahinna | Nuwara Eliya | — | 42,422 | — |
| New | LK-2316 | Norwood | Nuwara Eliya | — | 161,367 | — |
| New | LK-2313 | Thalawakele | Nuwara Eliya | — | 129,531 | — |
| Altered | LK-9118 | Balangoda | Ratnapura | 81,563 | 74,893 | <span style="color:red">▼</span> -8.2% |
| Altered | LK-9103 | Eheliyagoda | Ratnapura | 88,022 | 74,071 | <span style="color:red">▼</span> -15.8% |
| Altered | LK-9106 | Kuruvita | Ratnapura | 75,104 | 97,966 | <span style="color:green">▲</span> +30.4% |
| New | LK-9119 | Kalthota | Ratnapura | — | 13,018 | — |

---

## A5. Largest Change in Religious Proportion by DSD

For each DSD, the religion whose share of the local population changed most between 2012 and 2024.

*Altered, new, and removed DSDs excluded. Religions with <1% of national count or <1,000 people in the DSD are excluded.*

| DSD | District | Religion | Share 2012 | Share 2024 | Change |
|---|---|---|---:|---:|---:|
| Koralai Pattu Central | Batticaloa | Islam | 97.2% | 0.3% | <span style="color:red">▼</span> -96.9% |
| Kolonnawa | Colombo | Islam | 23.1% | 31.3% | <span style="color:green">▲</span> +8.3% |
| Dehiwala | Colombo | Islam | 22.6% | 30.4% | <span style="color:green">▲</span> +7.8% |
| Puthukkudiyiruppu | Mullaitivu | Hindu | 84.8% | 78.6% | <span style="color:red">▼</span> -6.2% |
| Nallur | Jaffna | Hindu | 90.4% | 85.9% | <span style="color:red">▼</span> -4.5% |
| Mannar Town | Mannar | RomanCatholic | 54.8% | 50.6% | <span style="color:red">▼</span> -4.1% |
| Wattala | Gampaha | Hindu | 13.0% | 16.9% | <span style="color:green">▲</span> +3.9% |
| Galle 4 Gravets | Galle | Islam | 32.3% | 36.0% | <span style="color:green">▲</span> +3.7% |
| Beruwala | Kalutara | Islam | 34.7% | 38.2% | <span style="color:green">▲</span> +3.5% |
| Mundel | Puttalam | Islam | 38.6% | 41.9% | <span style="color:green">▲</span> +3.3% |
| Akurana | Kandy | Islam | 64.9% | 67.9% | <span style="color:green">▲</span> +3.0% |
| Negombo | Gampaha | Islam | 14.3% | 17.2% | <span style="color:green">▲</span> +2.9% |
| Mawanella | Kegalle | Islam | 30.4% | 33.3% | <span style="color:green">▲</span> +2.8% |
| Panadura | Kalutara | Islam | 14.4% | 17.2% | <span style="color:green">▲</span> +2.8% |
| Vadamaradchi North (Point Pedro) | Jaffna | Hindu | 83.9% | 86.4% | <span style="color:green">▲</span> +2.5% |
| Vavuniya | Vavuniya | Hindu | 78.3% | 75.8% | <span style="color:red">▼</span> -2.5% |
| Nattandiya | Puttalam | RomanCatholic | 40.6% | 38.2% | <span style="color:red">▼</span> -2.4% |
| Puttalam | Puttalam | Islam | 64.2% | 66.6% | <span style="color:green">▲</span> +2.4% |
| Jaffna | Jaffna | RomanCatholic | 52.9% | 50.6% | <span style="color:red">▼</span> -2.3% |
| Kelaniya | Gampaha | RomanCatholic | 9.8% | 7.7% | <span style="color:red">▼</span> -2.1% |
| Nanaddan | Mannar | RomanCatholic | 68.4% | 66.4% | <span style="color:red">▼</span> -2.0% |
| Dankotuwa | Puttalam | RomanCatholic | 29.8% | 27.9% | <span style="color:red">▼</span> -1.9% |
| Attanagalla | Gampaha | Islam | 12.4% | 14.4% | <span style="color:green">▲</span> +1.9% |
| Katana | Gampaha | RomanCatholic | 32.0% | 34.0% | <span style="color:green">▲</span> +1.9% |
| Thimbirigasyaya | Colombo | Hindu | 22.5% | 24.4% | <span style="color:green">▲</span> +1.9% |
| Udunuwara | Kandy | Islam | 24.5% | 26.4% | <span style="color:green">▲</span> +1.9% |
| Colombo | Colombo | Hindu | 22.7% | 24.6% | <span style="color:green">▲</span> +1.9% |
| Kaduwela | Colombo | Buddhist | 90.4% | 92.3% | <span style="color:green">▲</span> +1.9% |
| Udapalatha | Kandy | Islam | 22.7% | 24.4% | <span style="color:green">▲</span> +1.8% |
| Karachchi | Kilinochchi | Hindu | 83.1% | 81.4% | <span style="color:red">▼</span> -1.7% |
| Kuchchaweli | Trincomalee | Islam | 64.1% | 65.8% | <span style="color:green">▲</span> +1.7% |
| Manmunai North | Batticaloa | RomanCatholic | 19.0% | 17.4% | <span style="color:red">▼</span> -1.6% |
| Muthur | Trincomalee | Islam | 62.0% | 63.5% | <span style="color:green">▲</span> +1.5% |
| Manmunai South & Eruvil Pattu | Batticaloa | Hindu | 93.9% | 95.4% | <span style="color:green">▲</span> +1.4% |
| Koralai Pattu North | Batticaloa | OtherChristian | 12.1% | 13.5% | <span style="color:green">▲</span> +1.4% |
| Mahawewa | Puttalam | RomanCatholic | 51.8% | 50.4% | <span style="color:red">▼</span> -1.4% |
| Kinniya | Trincomalee | Islam | 95.8% | 97.1% | <span style="color:green">▲</span> +1.4% |
| Kalpitiya | Puttalam | RomanCatholic | 32.3% | 33.6% | <span style="color:green">▲</span> +1.4% |
| Chilaw | Puttalam | RomanCatholic | 45.7% | 44.4% | <span style="color:red">▼</span> -1.3% |
| Gampaha | Gampaha | Buddhist | 87.6% | 88.8% | <span style="color:green">▲</span> +1.2% |
| Maharagama | Colombo | Buddhist | 92.0% | 93.2% | <span style="color:green">▲</span> +1.2% |
| Sri Jayawardanapura Kotte | Colombo | OtherChristian | 4.7% | 3.5% | <span style="color:red">▼</span> -1.2% |
| Mahara | Gampaha | RomanCatholic | 8.8% | 7.6% | <span style="color:red">▼</span> -1.2% |
| Thenmaradchi (Chavakachcheri) | Jaffna | Hindu | 92.7% | 91.7% | <span style="color:red">▼</span> -1.0% |
| Valikamam South West (Sandilipay) | Jaffna | Hindu | 75.1% | 76.1% | <span style="color:green">▲</span> +0.9% |
| Valikamam North (Thllippalai) | Jaffna | Hindu | 85.8% | 84.9% | <span style="color:red">▼</span> -0.9% |
| Town & Gravets | Trincomalee | Hindu | 49.0% | 48.2% | <span style="color:red">▼</span> -0.9% |
| Wennappuwa | Puttalam | RomanCatholic | 78.4% | 77.6% | <span style="color:red">▼</span> -0.8% |
| Hali-Ela | Badulla | Hindu | 29.0% | 29.7% | <span style="color:green">▲</span> +0.8% |
| Manmunai West | Batticaloa | Hindu | 97.2% | 97.9% | <span style="color:green">▲</span> +0.7% |

---

*Data from the 2012 and 2024 Sri Lanka Census, accessed via [lanka_data](https://pypi.org/project/lanka-data/). Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*
