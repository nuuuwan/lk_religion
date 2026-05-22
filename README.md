# lk_religion

Analyses of Sri Lanka's religious demographics, comparing the **2012 Census** and **2024 Census**.

Each analysis now lives in its own folder under [`analyses/`](analyses/), together with its own README, workflow script, and related data files. The sections below are copied from those child READMEs.

- [`analyses/a1_national_totals/`](analyses/a1_national_totals/)
- [`analyses/a2_by_district/`](analyses/a2_by_district/)
- [`analyses/a4_by_dsd/`](analyses/a4_by_dsd/)
- [`analyses/a6_by_province/`](analyses/a6_by_province/)
- [`analyses/a7_by_dsd/`](analyses/a7_by_dsd/)
- [`analyses/a8_by_country/`](analyses/a8_by_country/)

---

## A1. National Population by Religion

![A1 representative chart](analyses/a1_national_totals/chart.png)

| Religion | 2012 | 2024 | Change | Annual Growth | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Buddhist | 14,271,183 | 15,199,093 | +927,910 🟩 | +0.53% 🟩 | 70.1% | 69.8% | -0.3 🟥 pp |
| Hindu | 2,561,142 | 2,734,839 | +173,697 🟩 | +0.55% 🟩 | 12.6% | 12.6% | 0.0 pp |
| Islam | 1,967,008 | 2,337,379 | +370,371 🟩 | +1.45% 🟩 | 9.7% | 10.7% | +1.1 🟩 pp |
| RomanCatholic | 1,261,136 | 1,224,348 | -36,788 🟥 | -0.25% 🟥 | 6.2% | 5.6% | -0.6 🟥 pp |
| OtherChristian | 290,920 | 282,185 | -8,735 🟥 | -0.25% 🟥 | 1.4% | 1.3% | -0.1 🟥 pp |
| Other | 6,387 | 3,956 | -2,431 🟥 | -3.91% 🟥 | 0.0% | 0.0% | 0.0 pp |
| **Total** | **20,357,776** | **21,781,800** | **+1,424,024 🟩** | **+0.57% 🟩** | **100.0%** | **100.0%** | **0.0 pp** |

### Commentary

- Sri Lanka's total population grew from **20,357,776** (2012) to **21,781,800** (2024), an increase of **+1,424,024** at an annual rate of **+0.57%**.
- **Buddhism** remains the dominant religion, accounting for **69.8%** of the population in 2024, growing at **+0.53%** per year.
- **Islam** has the fastest growth rate among major religions at **+1.45%** per year, reaching a share of **10.7%** in 2024.
- **Roman Catholic** and **Other Christian** communities show slight declines over the period.

---

## A2. Religion by District: Key Trends

![A2 district change maps](analyses/a2_by_district/chart.png)

District labels show the **district name** and **change in share of population (pp)**. Districts are shaded by **change in share of population (pp)** from **red (decline)** to **green (growth)**. Districts with absolute share change **< 1.0pp** are shown in **white**.

Tables list only rows where absolute share change is **> 1.0pp**.

### Buddhist

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mannar `LK-42` | 0.0% | 1,809 | 382 | -1,427 🟥 | 1.8% | 0.3% | -1.5pp 🟥 |
| Ampara `LK-52` | 1.8% | 251,427 | 276,176 | +24,749 🟩 | 38.7% | 37.1% | -1.6pp 🟥 |
| Trincomalee `LK-53` | 0.7% | 99,344 | 106,919 | +7,575 🟩 | 26.2% | 24.1% | -2.0pp 🟥 |

***Trincomalee** saw the steepest share decline at **-2.0pp**. **Ampara** had the largest absolute increase (**+24,749**).*

### Hindu

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Kilinochchi `LK-45` | 4.0% | 92,986 | 110,258 | +17,272 🟩 | 81.9% | 80.7% | -1.3pp 🟥 |
| Batticaloa `LK-51` | 13.7% | 338,882 | 374,836 | +35,954 🟩 | 64.4% | 62.9% | -1.5pp 🟥 |
| Trincomalee `LK-53` | 4.0% | 98,442 | 108,050 | +9,608 🟩 | 25.9% | 24.4% | -1.5pp 🟥 |
| Mullaitivu `LK-44` | 3.2% | 69,377 | 88,738 | +19,361 🟩 | 75.3% | 72.4% | -2.9pp 🟥 |
| Vavuniya `LK-43` | 4.2% | 119,400 | 114,504 | -4,896 🟥 | 69.4% | 66.5% | -2.9pp 🟥 |
| Mannar `LK-42` | 1.0% | 24,027 | 26,214 | +2,187 🟩 | 24.1% | 21.2% | -2.9pp 🟥 |

***Mannar** saw the steepest share decline at **-2.9pp**. **Batticaloa** had the largest absolute increase (**+35,954**).*

### Islam

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mannar `LK-42` | 1.4% | 16,512 | 33,883 | +17,371 🟩 | 16.6% | 27.4% | +10.8pp 🟩 |
| Trincomalee `LK-53` | 8.8% | 159,418 | 205,664 | +46,246 🟩 | 42.0% | 46.5% | +4.4pp 🟩 |
| Vavuniya `LK-43` | 0.8% | 11,972 | 17,775 | +5,803 🟩 | 7.0% | 10.3% | +3.4pp 🟩 |
| Ampara `LK-52` | 14.5% | 281,987 | 339,896 | +57,909 🟩 | 43.4% | 45.7% | +2.2pp 🟩 |
| Puttalam `LK-62` | 7.6% | 150,404 | 176,963 | +26,559 🟩 | 19.7% | 21.6% | +1.9pp 🟩 |
| Batticaloa `LK-51` | 6.9% | 134,065 | 161,494 | +27,429 🟩 | 25.5% | 27.1% | +1.6pp 🟩 |
| Kalutara `LK-13` | 5.9% | 114,556 | 138,230 | +23,674 🟩 | 9.4% | 10.6% | +1.2pp 🟩 |
| Kegalle `LK-92` | 3.1% | 61,164 | 72,616 | +11,452 🟩 | 7.3% | 8.3% | +1.1pp 🟩 |

***Mannar** gained the most share at **+10.8pp**. **Kegalle** had the smallest share gain at **+1.1pp**. **Ampara** had the largest absolute increase (**+57,909**).*

### Roman Catholic

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mullaitivu `LK-44` | 1.1% | 9,063 | 13,982 | +4,919 🟩 | 9.8% | 11.4% | +1.6pp 🟩 |
| Colombo `LK-11` | 11.4% | 162,260 | 139,882 | -22,378 🟥 | 7.0% | 5.9% | -1.1pp 🟥 |
| Gampaha `LK-12` | 36.1% | 449,398 | 442,291 | -7,107 🟥 | 19.5% | 18.2% | -1.3pp 🟥 |
| Vavuniya `LK-43` | 1.0% | 15,305 | 12,785 | -2,520 🟥 | 8.9% | 7.4% | -1.5pp 🟥 |
| Puttalam `LK-62` | 19.7% | 240,221 | 240,975 | +754 🟩 | 31.5% | 29.4% | -2.1pp 🟥 |
| Mannar `LK-42` | 4.7% | 52,415 | 57,713 | +5,298 🟩 | 52.6% | 46.6% | -6.0pp 🟥 |

***Mullaitivu** gained the most share at **+1.6pp**. **Mannar** saw the steepest share decline at **-6.0pp**. **Mannar** had the largest absolute increase (**+5,298**).*

### Other Christian

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Mullaitivu `LK-44` | 2.2% | 3,664 | 6,315 | +2,651 🟩 | 4.0% | 5.2% | +1.2pp 🟩 |

***Mullaitivu** gained the most share at **+1.2pp**.*

### Other

| District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|

*No regions exceed the table share-change threshold.*

---

## A4. DSD Boundary Changes

![A4 representative chart](analyses/a4_by_dsd/chart.png)

Districts where the number of DSDs changed between censuses are listed below. Within those districts, DSDs whose population growth deviates from the national rate (+6.99% over 2012–2024) by more than 2× are flagged as **Altered** — their apparent demographic shifts likely reflect re-demarcation rather than genuine change.

**Districts with changed DSD boundaries:**

| District | DSDs 2012 | DSDs 2024 | Δ |
|---|---:|---:|---:|
| Nuwara Eliya `LK-23` | 5 | 10 | +5 🟩 |
| Galle `LK-31` | 19 | 22 | +3 🟩 |
| Batticaloa `LK-51` | 14 | 13 | -1 🟥 |
| Ampara `LK-52` | 20 | 19 | -1 🟥 |
| Ratnapura `LK-91` | 17 | 18 | +1 🟩 |

**New, Altered, and Removed DSDs:**

| Status | DSD | District | Pop 2012 | Pop 2024 | Pop Change |
|---|---|---|---:|---:|---:|
| Removed | LK-5224 `LK-5224` | Ampara `LK-52` | 44,632 | — | — |
| Altered | Addalaichenai `LK-5233` | Ampara `LK-52` | 41,968 | 53,214 | +26.8% 🟩 |
| Altered | Irakkamam `LK-5234` | Ampara `LK-52` | 14,383 | 17,671 | +22.9% 🟩 |
| Altered | Kalmunai `LK-5221` | Ampara `LK-52` | 29,800 | 52,798 | +77.2% 🟩 |
| Altered | Pottuvil `LK-5248` | Ampara `LK-52` | 34,809 | 42,908 | +23.3% 🟩 |
| Removed | Koralai Pattu `LK-5109` | Batticaloa `LK-51` | 23,376 | — | — |
| Removed | LK-5112 `LK-5112` | Batticaloa `LK-51` | 75,478 | — | — |
| Altered | Eravur Pattu `LK-5115` | Batticaloa `LK-51` | 24,643 | 94,237 | +282.4% 🟩 |
| New | Eravur Town `LK-5139` | Batticaloa `LK-51` | — | 26,468 | — |
| Altered | Baddegama `LK-3127` | Galle `LK-31` | 75,008 | 50,956 | -32.1% 🟥 |
| Altered | Hikkaduwa `LK-3136` | Galle `LK-31` | 101,909 | 26,216 | -74.3% 🟥 |
| New | Madampagama `LK-3138` | Galle `LK-31` | — | 33,408 | — |
| New | Rathgama `LK-3137` | Galle `LK-31` | — | 41,456 | — |
| New | Wanduramba `LK-3128` | Galle `LK-31` | — | 27,702 | — |
| Altered | Ambagamuwa Korale `LK-2315` | Nuwara Eliya `LK-23` | 205,723 | 42,538 | -79.3% 🟥 |
| Altered | Hanguranketa `LK-2306` | Nuwara Eliya `LK-23` | 88,528 | 58,931 | -33.4% 🟥 |
| Altered | Kothmale East `LK-2303` | Nuwara Eliya `LK-23` | 101,180 | 61,742 | -39.0% 🟥 |
| Altered | Nuwara Eliya `LK-2312` | Nuwara Eliya `LK-23` | 212,094 | 88,332 | -58.4% 🟥 |
| Altered | Walapane `LK-2309` | Nuwara Eliya `LK-23` | 104,119 | 65,287 | -37.3% 🟥 |
| New | Kothmale West `LK-2304` | Nuwara Eliya `LK-23` | — | 41,955 | — |
| New | Mathurata `LK-2307` | Nuwara Eliya `LK-23` | — | 33,175 | — |
| New | Nildandahinna `LK-2310` | Nuwara Eliya `LK-23` | — | 42,422 | — |
| New | Norwood `LK-2316` | Nuwara Eliya `LK-23` | — | 161,367 | — |
| New | Thalawakele `LK-2313` | Nuwara Eliya `LK-23` | — | 129,531 | — |
| Altered | Balangoda `LK-9118` | Ratnapura `LK-91` | 81,563 | 74,893 | -8.2% 🟥 |
| Altered | Eheliyagoda `LK-9103` | Ratnapura `LK-91` | 88,022 | 74,071 | -15.8% 🟥 |
| Altered | Kuruvita `LK-9106` | Ratnapura `LK-91` | 75,104 | 97,966 | +30.4% 🟩 |
| New | Kalthota `LK-9119` | Ratnapura `LK-91` | — | 13,018 | — |

---

## A6. Religion by Province: Key Trends

![A6 province change maps](analyses/a6_by_province/chart.png)

Province labels show the **province name** and **change in share of population (pp)**. Provinces are shaded by **change in share of population (pp)** from **red (decline)** to **green (growth)**. Provinces with absolute share change **< 1.0pp** are shown in **white**.

Tables list only rows where absolute share change is **> 1.0pp**.

### Buddhist

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Eastern `LK-5` | 2.6% | 357,052 | 389,119 | +32,067 🟩 | 23.0% | 21.8% | -1.1pp 🟥 |

***Eastern** saw the steepest share decline at **-1.1pp**.*

### Hindu

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Eastern `LK-5` | 21.8% | 540,153 | 597,472 | +57,319 🟩 | 34.7% | 33.5% | -1.2pp 🟥 |
| Northern `LK-4` | 30.3% | 789,045 | 829,235 | +40,190 🟩 | 74.4% | 72.1% | -2.3pp 🟥 |

***Northern** saw the steepest share decline at **-2.3pp**.*

### Islam

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Eastern `LK-5` | 30.2% | 575,470 | 707,054 | +131,584 🟩 | 37.0% | 39.7% | +2.7pp 🟩 |
| Northern `LK-4` | 2.6% | 33,427 | 60,683 | +27,256 🟩 | 3.1% | 5.3% | +2.1pp 🟩 |
| North Western `LK-6` | 13.7% | 268,214 | 320,262 | +52,048 🟩 | 11.3% | 12.4% | +1.1pp 🟩 |

***Eastern** gained the most share at **+2.7pp**. **North Western** had the smallest share gain at **+1.1pp**.*

### Roman Catholic

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| North Western `LK-6` | 23.0% | 283,928 | 281,248 | -2,680 🟥 | 11.9% | 10.9% | -1.1pp 🟥 |

***North Western** saw the steepest share decline at **-1.1pp**.*

### Other Christian

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|

*No regions exceed the table share-change threshold.*

### Other

| Province | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|

*No regions exceed the table share-change threshold.*

---

## A7. Religion by DSD: Key Trends

![A7 DSD change maps](analyses/a7_by_dsd/chart.png)

DSDs are shaded by **change in share of population (pp)** from **red (decline)** to **green (growth)**. DSD labels are omitted due to map density.  DSDs with absolute share change **< 1.0pp** are shown in **white**.

Tables list only rows where absolute share change is **> 1.0pp**.

*New, removed, and altered DSDs from A4 are excluded to avoid boundary-change artifacts.*

### Buddhist

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Vavuniya North `LK-4303` | Vavuniya | 0.0% | 511 | 1,149 | +638 🟩 | 4.4% | 7.8% | +3.4pp 🟩 |
| Haldummulla `LK-8142` | Badulla | 0.1% | 19,698 | 21,455 | +1,757 🟩 | 52.4% | 55.3% | +2.9pp 🟩 |
| Kotapola `LK-3206` | Matara | 0.4% | 51,188 | 50,977 | -211 🟥 | 80.9% | 83.6% | +2.6pp 🟩 |
| Kalawana `LK-9133` | Ratnapura | 0.3% | 43,847 | 44,599 | +752 🟩 | 85.5% | 87.9% | +2.4pp 🟩 |
| Meegahakiula `LK-8109` | Badulla | 0.1% | 17,640 | 20,824 | +3,184 🟩 | 89.5% | 91.8% | +2.3pp 🟩 |
| Karuwalagaswewa `LK-6209` | Puttalam | 0.2% | 21,391 | 24,542 | +3,151 🟩 | 91.3% | 93.6% | +2.3pp 🟩 |
| Rambewa `LK-7118` | Anuradhapura | 0.2% | 30,904 | 34,412 | +3,508 🟩 | 84.0% | 86.3% | +2.3pp 🟩 |
| Chilaw `LK-6233` | Puttalam | 0.2% | 22,855 | 24,717 | +1,862 🟩 | 36.6% | 38.8% | +2.3pp 🟩 |
| Dankotuwa `LK-6248` | Puttalam | 0.3% | 41,674 | 43,375 | +1,701 🟩 | 66.8% | 69.0% | +2.2pp 🟩 |
| Nallur `LK-4133` | Jaffna | 0.0% | 273 | 1,718 | +1,445 🟩 | 0.4% | 2.4% | +2.0pp 🟩 |
| Kaduwela `LK-1109` | Colombo | 1.8% | 227,939 | 256,548 | +28,609 🟩 | 90.4% | 92.3% | +1.9pp 🟩 |
| Mahawewa `LK-6239` | Puttalam | 0.2% | 23,204 | 23,033 | -171 🟥 | 45.4% | 47.2% | +1.7pp 🟩 |
| Koralai Pattu Central `LK-5104` | Batticaloa | 0.0% | 67 | 569 | +502 🟩 | 0.3% | 2.0% | +1.7pp 🟩 |
| Kuchchaweli `LK-5306` | Trincomalee | 0.0% | 783 | 1,534 | +751 🟩 | 2.4% | 3.8% | +1.5pp 🟩 |
| Laggala `LK-2224` | Matale | 0.1% | 11,897 | 16,253 | +4,356 🟩 | 98.2% | 99.7% | +1.5pp 🟩 |
| Gangawata Korale `LK-2130` | Kandy | 0.8% | 112,495 | 110,984 | -1,511 🟥 | 70.9% | 72.4% | +1.4pp 🟩 |
| Madampe `LK-6236` | Puttalam | 0.2% | 34,803 | 36,282 | +1,479 🟩 | 72.6% | 74.1% | +1.4pp 🟩 |
| Kurunegala `LK-6154` | Kurunegala | 0.5% | 64,117 | 71,927 | +7,810 🟩 | 79.4% | 80.8% | +1.4pp 🟩 |
| Ayagama `LK-9130` | Ratnapura | 0.2% | 26,626 | 26,217 | -409 🟥 | 86.2% | 87.6% | +1.4pp 🟩 |
| Gampaha `LK-1224` | Gampaha | 1.3% | 173,095 | 182,606 | +9,511 🟩 | 87.6% | 88.8% | +1.2pp 🟩 |
| Thawalama `LK-3118` | Galle | 0.2% | 30,335 | 29,207 | -1,128 🟥 | 93.0% | 94.2% | +1.2pp 🟩 |
| Maharagama `LK-1121` | Colombo | 1.3% | 180,631 | 183,093 | +2,462 🟩 | 92.0% | 93.2% | +1.2pp 🟩 |
| Nuwaragam Palatha East `LK-7133` | Anuradhapura | 0.5% | 64,681 | 71,538 | +6,857 🟩 | 92.7% | 94.0% | +1.2pp 🟩 |
| Pitabaddara `LK-3203` | Matara | 0.3% | 47,583 | 45,984 | -1,599 🟥 | 93.0% | 94.1% | +1.1pp 🟩 |
| Nivithigala `LK-9136` | Ratnapura | 0.3% | 49,161 | 49,271 | +110 🟩 | 81.8% | 82.9% | +1.1pp 🟩 |
| Imbulpe `LK-9115` | Ratnapura | 0.4% | 50,082 | 55,075 | +4,993 🟩 | 84.2% | 85.3% | +1.1pp 🟩 |
| Katharagama `LK-8227` | Monaragala | 0.1% | 17,342 | 17,477 | +135 🟩 | 95.2% | 96.2% | +1.1pp 🟩 |
| Thimbirigasyaya `LK-1127` | Colombo | 0.7% | 113,810 | 101,553 | -12,257 🟥 | 47.9% | 46.8% | -1.1pp 🟥 |
| Mihinthale `LK-7130` | Anuradhapura | 0.3% | 33,046 | 40,807 | +7,761 🟩 | 93.6% | 92.5% | -1.1pp 🟥 |
| Musali `LK-4215` | Mannar | 0.0% | 129 | 83 | -46 🟥 | 1.6% | 0.5% | -1.1pp 🟥 |
| Lunugala `LK-8119` | Badulla | 0.1% | 12,976 | 12,807 | -169 🟥 | 41.3% | 40.2% | -1.2pp 🟥 |
| Mallawapitiya `LK-6157` | Kurunegala | 0.3% | 41,729 | 46,464 | +4,735 🟩 | 79.3% | 78.1% | -1.2pp 🟥 |
| Negombo `LK-1203` | Gampaha | 0.1% | 15,732 | 13,506 | -2,226 🟥 | 11.1% | 9.8% | -1.3pp 🟥 |
| Valikamam North (Thllippalai) `LK-4112` | Jaffna | 0.0% | 431 | 64 | -367 🟥 | 1.5% | 0.1% | -1.3pp 🟥 |
| Weligama `LK-3239` | Matara | 0.5% | 65,046 | 66,983 | +1,937 🟩 | 89.3% | 88.0% | -1.3pp 🟥 |
| Kundasale `LK-2127` | Kandy | 0.8% | 103,484 | 115,594 | +12,110 🟩 | 81.4% | 80.1% | -1.4pp 🟥 |
| Mannar Town `LK-4203` | Mannar | 0.0% | 811 | 96 | -715 🟥 | 1.6% | 0.2% | -1.4pp 🟥 |
| Thunukkai `LK-4403` | Mullaitivu | 0.0% | 168 | 31 | -137 🟥 | 1.7% | 0.3% | -1.4pp 🟥 |
| Panduwasnuwara West `LK-6145` | Kurunegala | 0.4% | 55,271 | 58,481 | +3,210 🟩 | 83.6% | 82.2% | -1.4pp 🟥 |
| Medagama `LK-8209` | Monaragala | 0.3% | 30,810 | 37,662 | +6,852 🟩 | 85.9% | 84.4% | -1.4pp 🟥 |
| Kelaniya `LK-1236` | Gampaha | 0.7% | 102,634 | 97,990 | -4,644 🟥 | 74.7% | 73.3% | -1.5pp 🟥 |
| Attanagalla `LK-1227` | Gampaha | 1.1% | 151,786 | 164,206 | +12,420 🟩 | 84.5% | 83.0% | -1.5pp 🟥 |
| Panadura `LK-1303` | Kalutara | 1.0% | 143,301 | 144,521 | +1,220 🟩 | 78.6% | 77.1% | -1.5pp 🟥 |
| Rideegama `LK-6163` | Kurunegala | 0.6% | 75,598 | 80,308 | +4,710 🟩 | 85.2% | 83.7% | -1.5pp 🟥 |
| Udunuwara `LK-2139` | Kandy | 0.6% | 79,869 | 85,290 | +5,421 🟩 | 72.0% | 70.5% | -1.5pp 🟥 |
| Vavuniya South `LK-4306` | Vavuniya | 0.1% | 12,532 | 13,946 | +1,414 🟩 | 95.5% | 94.0% | -1.6pp 🟥 |
| Thambalagamuwa `LK-5318` | Trincomalee | 0.1% | 6,760 | 7,440 | +680 🟩 | 23.7% | 22.1% | -1.6pp 🟥 |
| Wattala `LK-1218` | Gampaha | 0.4% | 52,405 | 51,544 | -861 🟥 | 29.9% | 28.2% | -1.6pp 🟥 |
| Welimada `LK-8130` | Badulla | 0.5% | 71,215 | 72,755 | +1,540 🟩 | 70.6% | 69.0% | -1.7pp 🟥 |
| Ukuwela `LK-2233` | Matale | 0.3% | 43,744 | 45,225 | +1,481 🟩 | 64.3% | 62.5% | -1.8pp 🟥 |
| Manthai East `LK-4406` | Mullaitivu | 0.0% | 163 | 34 | -129 🟥 | 2.3% | 0.4% | -1.8pp 🟥 |
| Haputale `LK-8139` | Badulla | 0.2% | 26,212 | 24,432 | -1,780 🟥 | 52.6% | 50.6% | -2.0pp 🟥 |
| Udapalatha `LK-2151` | Kandy | 0.4% | 50,471 | 54,676 | +4,205 🟩 | 55.0% | 53.0% | -2.0pp 🟥 |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.0% | 672 | 46 | -626 🟥 | 2.2% | 0.2% | -2.1pp 🟥 |
| Pathadumbara `LK-2112` | Kandy | 0.5% | 65,000 | 66,522 | +1,522 🟩 | 73.3% | 71.2% | -2.1pp 🟥 |
| Kobeigane `LK-6139` | Kurunegala | 0.2% | 31,165 | 34,325 | +3,160 🟩 | 86.6% | 84.4% | -2.2pp 🟥 |
| Manthai West `LK-4206` | Mannar | 0.0% | 350 | 19 | -331 🟥 | 2.4% | 0.1% | -2.3pp 🟥 |
| Madhu `LK-4209` | Mannar | 0.0% | 268 | 101 | -167 🟥 | 3.5% | 1.1% | -2.4pp 🟥 |
| Morawewa `LK-5312` | Trincomalee | 0.0% | 5,736 | 6,393 | +657 🟩 | 72.0% | 69.5% | -2.4pp 🟥 |
| Beruwala `LK-1324` | Kalutara | 0.7% | 91,957 | 96,273 | +4,316 🟩 | 55.7% | 53.2% | -2.5pp 🟥 |
| Akurana `LK-2109` | Kandy | 0.1% | 18,739 | 19,167 | +428 🟩 | 29.6% | 27.0% | -2.6pp 🟥 |
| Welipitiya `LK-3221` | Matara | 0.3% | 45,531 | 47,466 | +1,935 🟩 | 87.4% | 84.8% | -2.6pp 🟥 |
| Oddusuddan `LK-4412` | Mullaitivu | 0.0% | 622 | 245 | -377 🟥 | 4.0% | 1.3% | -2.6pp 🟥 |
| Colombo `LK-1103` | Colombo | 0.3% | 61,448 | 47,726 | -13,722 🟥 | 19.0% | 16.3% | -2.7pp 🟥 |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.0% | 237 | 13 | -224 🟥 | 2.8% | 0.1% | -2.7pp 🟥 |
| Kuliyapitiya East `LK-6169` | Kurunegala | 0.3% | 36,275 | 39,425 | +3,150 🟩 | 67.1% | 64.4% | -2.7pp 🟥 |
| Mawanella `LK-9206` | Kegalle | 0.6% | 76,124 | 82,393 | +6,269 🟩 | 68.1% | 65.4% | -2.8pp 🟥 |
| Horowpathana `LK-7124` | Anuradhapura | 0.2% | 26,965 | 28,932 | +1,967 🟩 | 72.9% | 70.1% | -2.8pp 🟥 |
| Kahatagasdigiliya `LK-7121` | Anuradhapura | 0.2% | 31,772 | 34,073 | +2,301 🟩 | 78.8% | 75.9% | -2.9pp 🟥 |
| Katana `LK-1206` | Gampaha | 0.9% | 141,353 | 137,806 | -3,547 🟥 | 60.1% | 57.1% | -2.9pp 🟥 |
| Lankapura `LK-7209` | Polonnaruwa | 0.2% | 25,849 | 26,904 | +1,055 🟩 | 70.9% | 67.8% | -3.1pp 🟥 |
| Galle 4 Gravets `LK-3139` | Galle | 0.5% | 66,840 | 67,502 | +662 🟩 | 65.7% | 62.3% | -3.4pp 🟥 |
| Seruvila `LK-5330` | Trincomalee | 0.1% | 8,805 | 9,787 | +982 🟩 | 64.6% | 61.1% | -3.4pp 🟥 |
| Ratmalana `LK-1131` | Colombo | 0.4% | 66,808 | 57,385 | -9,423 🟥 | 70.0% | 65.2% | -4.8pp 🟥 |
| Kolonnawa `LK-1106` | Colombo | 0.8% | 123,787 | 122,559 | -1,228 🟥 | 64.6% | 57.3% | -7.3pp 🟥 |
| Dehiwala `LK-1130` | Colombo | 0.3% | 48,310 | 43,573 | -4,737 🟥 | 54.3% | 46.4% | -7.9pp 🟥 |

***Vavuniya North** gained the most share at **+3.4pp**. **Dehiwala** saw the steepest share decline at **-7.9pp**. **Kaduwela** had the largest absolute increase (**+28,609**).*

### Hindu

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Koralai Pattu Central `LK-5104` | Batticaloa | 1.0% | 580 | 23,383 | +22,803 🟩 | 2.3% | 81.3% | +79.0pp 🟩 |
| Wattala `LK-1218` | Gampaha | 1.4% | 22,782 | 30,805 | +8,023 🟩 | 13.0% | 16.9% | +3.9pp 🟩 |
| Dehiwala `LK-1130` | Colombo | 0.6% | 10,783 | 14,406 | +3,623 🟩 | 12.1% | 15.4% | +3.2pp 🟩 |
| Morawewa `LK-5312` | Trincomalee | 0.1% | 833 | 1,200 | +367 🟩 | 10.5% | 13.1% | +2.6pp 🟩 |
| Vadamaradchi North (Point Pedro) `LK-4127` | Jaffna | 1.7% | 39,886 | 37,472 | -2,414 🟥 | 83.9% | 86.4% | +2.5pp 🟩 |
| Ratmalana `LK-1131` | Colombo | 0.3% | 5,739 | 7,316 | +1,577 🟩 | 6.0% | 8.3% | +2.3pp 🟩 |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.5% | 7,176 | 11,271 | +4,095 🟩 | 84.1% | 86.4% | +2.3pp 🟩 |
| Kelaniya `LK-1236` | Gampaha | 0.4% | 6,415 | 8,886 | +2,471 🟩 | 4.7% | 6.6% | +2.0pp 🟩 |
| Lunugala `LK-8119` | Badulla | 0.7% | 15,284 | 16,140 | +856 🟩 | 48.7% | 50.6% | +1.9pp 🟩 |
| Thimbirigasyaya `LK-1127` | Colombo | 2.4% | 53,469 | 52,962 | -507 🟥 | 22.5% | 24.4% | +1.9pp 🟩 |
| Colombo `LK-1103` | Colombo | 3.2% | 73,374 | 71,811 | -1,563 🟥 | 22.7% | 24.6% | +1.9pp 🟩 |
| Haputale `LK-8139` | Badulla | 0.8% | 17,312 | 17,674 | +362 🟩 | 34.8% | 36.6% | +1.8pp 🟩 |
| Passara `LK-8118` | Badulla | 0.8% | 17,178 | 18,256 | +1,078 🟩 | 35.2% | 36.8% | +1.6pp 🟩 |
| Kundasale `LK-2127` | Kandy | 0.7% | 12,216 | 16,116 | +3,900 🟩 | 9.6% | 11.2% | +1.5pp 🟩 |
| Manmunai South & Eruvil Pattu `LK-5136` | Batticaloa | 2.7% | 57,103 | 59,997 | +2,894 🟩 | 93.9% | 95.4% | +1.4pp 🟩 |
| Panvila `LK-2115` | Kandy | 0.6% | 13,720 | 13,754 | +34 🟩 | 52.2% | 53.6% | +1.4pp 🟩 |
| Monaragala `LK-8215` | Monaragala | 0.3% | 5,927 | 7,625 | +1,698 🟩 | 12.0% | 13.4% | +1.4pp 🟩 |
| Seethawaka `LK-1115` | Colombo | 0.5% | 9,690 | 12,066 | +2,376 🟩 | 8.5% | 9.9% | +1.4pp 🟩 |
| Ella `LK-8136` | Badulla | 0.6% | 12,338 | 14,108 | +1,770 🟩 | 27.3% | 28.5% | +1.2pp 🟩 |
| Oddusuddan `LK-4412` | Mullaitivu | 0.7% | 13,421 | 15,685 | +2,264 🟩 | 85.4% | 86.4% | +1.1pp 🟩 |
| Ganga Ihala Korale `LK-2154` | Kandy | 0.3% | 6,229 | 6,018 | -211 🟥 | 11.3% | 10.2% | -1.1pp 🟥 |
| Puttalam `LK-6215` | Puttalam | 0.2% | 4,854 | 4,446 | -408 🟥 | 5.9% | 4.7% | -1.2pp 🟥 |
| Thunukkai `LK-4403` | Mullaitivu | 0.4% | 8,682 | 9,188 | +506 🟩 | 89.5% | 88.3% | -1.3pp 🟥 |
| Thawalama `LK-3118` | Galle | 0.1% | 1,661 | 1,183 | -478 🟥 | 5.1% | 3.8% | -1.3pp 🟥 |
| Manthai West `LK-4206` | Mannar | 0.3% | 6,127 | 7,488 | +1,361 🟩 | 41.5% | 40.1% | -1.4pp 🟥 |
| Maritimepattu `LK-4415` | Mullaitivu | 1.2% | 20,709 | 25,829 | +5,120 🟩 | 71.6% | 70.2% | -1.4pp 🟥 |
| Laggala `LK-2224` | Matale | 0.0% | 206 | 36 | -170 🟥 | 1.7% | 0.2% | -1.5pp 🟥 |
| Koralai Pattu North `LK-5103` | Batticaloa | 0.9% | 17,356 | 20,144 | +2,788 🟩 | 80.6% | 79.1% | -1.5pp 🟥 |
| Navithanveli `LK-5216` | Ampara | 0.5% | 10,271 | 11,635 | +1,364 🟩 | 54.8% | 53.2% | -1.6pp 🟥 |
| Karachchi `LK-4509` | Kilinochchi | 2.7% | 51,086 | 60,727 | +9,641 🟩 | 83.1% | 81.4% | -1.7pp 🟥 |
| Pitabaddara `LK-3203` | Matara | 0.1% | 3,092 | 2,094 | -998 🟥 | 6.0% | 4.3% | -1.8pp 🟥 |
| Meegahakiula `LK-8109` | Badulla | 0.1% | 1,883 | 1,767 | -116 🟥 | 9.5% | 7.8% | -1.8pp 🟥 |
| Welikanda `LK-7210` | Polonnaruwa | 0.1% | 3,508 | 3,245 | -263 🟥 | 10.4% | 8.5% | -1.9pp 🟥 |
| Thambalagamuwa `LK-5318` | Trincomalee | 0.2% | 4,873 | 5,089 | +216 🟩 | 17.1% | 15.1% | -2.0pp 🟥 |
| Kuchchaweli `LK-5306` | Trincomalee | 0.5% | 9,152 | 10,196 | +1,044 🟩 | 27.6% | 25.6% | -2.0pp 🟥 |
| Musali `LK-4215` | Mannar | 0.0% | 354 | 419 | +65 🟩 | 4.4% | 2.3% | -2.1pp 🟥 |
| Karaitivu `LK-5227` | Ampara | 0.5% | 9,788 | 10,919 | +1,131 🟩 | 58.1% | 56.0% | -2.1pp 🟥 |
| Haldummulla `LK-8142` | Badulla | 0.7% | 16,445 | 16,140 | -305 🟥 | 43.8% | 41.6% | -2.2pp 🟥 |
| Kotapola `LK-3206` | Matara | 0.3% | 9,430 | 7,749 | -1,681 🟥 | 14.9% | 12.7% | -2.2pp 🟥 |
| Kalawana `LK-9133` | Ratnapura | 0.2% | 6,789 | 5,584 | -1,205 🟥 | 13.2% | 11.0% | -2.2pp 🟥 |
| Mundel `LK-6218` | Puttalam | 0.4% | 9,328 | 9,244 | -84 🟥 | 15.1% | 12.7% | -2.4pp 🟥 |
| Poonakary `LK-4512` | Kilinochchi | 0.7% | 14,220 | 16,294 | +2,074 🟩 | 70.0% | 67.6% | -2.5pp 🟥 |
| Vavuniya `LK-4309` | Vavuniya | 4.0% | 92,034 | 88,683 | -3,351 🟥 | 78.3% | 75.8% | -2.5pp 🟥 |
| Islands North (Kayts) `LK-4103` | Jaffna | 0.2% | 5,401 | 5,170 | -231 🟥 | 54.7% | 52.1% | -2.6pp 🟥 |
| Koralai Pattu South `LK-5110` | Batticaloa | 1.1% | 24,280 | 25,536 | +1,256 🟩 | 92.9% | 90.2% | -2.6pp 🟥 |
| Mannar Town `LK-4203` | Mannar | 0.4% | 10,401 | 9,927 | -474 🟥 | 20.4% | 17.2% | -3.2pp 🟥 |
| Islands South (Velanai) `LK-4139` | Jaffna | 0.5% | 12,584 | 11,846 | -738 🟥 | 75.2% | 71.4% | -3.8pp 🟥 |
| Vavuniya North `LK-4303` | Vavuniya | 0.6% | 10,363 | 12,616 | +2,253 🟩 | 89.9% | 85.8% | -4.2pp 🟥 |
| Nallur `LK-4133` | Jaffna | 2.8% | 61,569 | 62,589 | +1,020 🟩 | 90.4% | 85.9% | -4.5pp 🟥 |
| Delft `LK-4142` | Jaffna | 0.0% | 1,439 | 1,002 | -437 🟥 | 37.6% | 31.7% | -5.9pp 🟥 |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.6% | 16,680 | 12,803 | -3,877 🟥 | 55.8% | 49.7% | -6.1pp 🟥 |
| Manmunai Pattu `LK-5127` | Batticaloa | 1.0% | 21,350 | 23,159 | +1,809 🟩 | 69.6% | 63.4% | -6.2pp 🟥 |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu | 1.4% | 20,209 | 31,073 | +10,864 🟩 | 84.8% | 78.6% | -6.2pp 🟥 |

***Koralai Pattu Central** gained the most share at **+79.0pp**. **Puthukkudiyiruppu** saw the steepest share decline at **-6.2pp**.*

### Islam

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Musali `LK-4215` | Mannar | 0.7% | 4,848 | 13,581 | +8,733 🟩 | 59.7% | 74.9% | +15.1pp 🟩 |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.4% | 6,909 | 9,146 | +2,237 🟩 | 23.1% | 35.5% | +12.4pp 🟩 |
| Mannar Town `LK-4203` | Mannar | 0.7% | 9,098 | 15,373 | +6,275 🟩 | 17.8% | 26.6% | +8.8pp 🟩 |
| Kolonnawa `LK-1106` | Colombo | 3.2% | 44,189 | 67,100 | +22,911 🟩 | 23.1% | 31.3% | +8.3pp 🟩 |
| Dehiwala `LK-1130` | Colombo | 1.4% | 20,109 | 28,538 | +8,429 🟩 | 22.6% | 30.4% | +7.8pp 🟩 |
| Manmunai Pattu `LK-5127` | Batticaloa | 0.5% | 7,565 | 11,254 | +3,689 🟩 | 24.6% | 30.8% | +6.2pp 🟩 |
| Madhu `LK-4209` | Mannar | 0.1% | 559 | 1,196 | +637 🟩 | 7.2% | 12.6% | +5.3pp 🟩 |
| Ratmalana `LK-1131` | Colombo | 0.7% | 10,837 | 13,852 | +3,015 🟩 | 11.3% | 15.7% | +4.4pp 🟩 |
| Galle 4 Gravets `LK-3139` | Galle | 1.9% | 32,865 | 39,021 | +6,156 🟩 | 32.3% | 36.0% | +3.7pp 🟩 |
| Beruwala `LK-1324` | Kalutara | 3.3% | 57,228 | 69,141 | +11,913 🟩 | 34.7% | 38.2% | +3.5pp 🟩 |
| Nanaddan `LK-4212` | Mannar | 0.1% | 668 | 1,405 | +737 🟩 | 3.7% | 7.1% | +3.4pp 🟩 |
| Manthai West `LK-4206` | Mannar | 0.1% | 1,339 | 2,328 | +989 🟩 | 9.1% | 12.5% | +3.4pp 🟩 |
| Thambalagamuwa `LK-5318` | Trincomalee | 1.0% | 16,256 | 20,286 | +4,030 🟩 | 57.0% | 60.3% | +3.3pp 🟩 |
| Mundel `LK-6218` | Puttalam | 1.5% | 23,770 | 30,384 | +6,614 🟩 | 38.6% | 41.9% | +3.3pp 🟩 |
| Lankapura `LK-7209` | Polonnaruwa | 0.6% | 10,377 | 12,589 | +2,212 🟩 | 28.5% | 31.7% | +3.3pp 🟩 |
| Vavuniya `LK-4309` | Vavuniya | 0.4% | 5,037 | 8,612 | +3,575 🟩 | 4.3% | 7.4% | +3.1pp 🟩 |
| Akurana `LK-2109` | Kandy | 2.3% | 41,117 | 48,201 | +7,084 🟩 | 64.9% | 67.9% | +3.0pp 🟩 |
| Kahatagasdigiliya `LK-7121` | Anuradhapura | 0.5% | 8,198 | 10,466 | +2,268 🟩 | 20.3% | 23.3% | +3.0pp 🟩 |
| Negombo `LK-1203` | Gampaha | 1.1% | 20,374 | 23,788 | +3,414 🟩 | 14.3% | 17.2% | +2.9pp 🟩 |
| Welikanda `LK-7210` | Polonnaruwa | 0.3% | 4,929 | 6,663 | +1,734 🟩 | 14.6% | 17.4% | +2.8pp 🟩 |
| Horowpathana `LK-7124` | Anuradhapura | 0.6% | 9,829 | 12,135 | +2,306 🟩 | 26.6% | 29.4% | +2.8pp 🟩 |
| Mawanella `LK-9206` | Kegalle | 2.0% | 34,008 | 41,933 | +7,925 🟩 | 30.4% | 33.3% | +2.8pp 🟩 |
| Kuliyapitiya East `LK-6169` | Kurunegala | 1.0% | 17,087 | 21,068 | +3,981 🟩 | 31.6% | 34.4% | +2.8pp 🟩 |
| Panadura `LK-1303` | Kalutara | 1.6% | 26,306 | 32,306 | +6,000 🟩 | 14.4% | 17.2% | +2.8pp 🟩 |
| Welipitiya `LK-3221` | Matara | 0.4% | 6,339 | 8,220 | +1,881 🟩 | 12.2% | 14.7% | +2.5pp 🟩 |
| Jaffna `LK-4136` | Jaffna | 0.1% | 1,732 | 2,881 | +1,149 🟩 | 3.4% | 5.9% | +2.5pp 🟩 |
| Pallama `LK-6227` | Puttalam | 0.3% | 3,977 | 5,235 | +1,258 🟩 | 16.3% | 18.7% | +2.5pp 🟩 |
| Seruvila `LK-5330` | Trincomalee | 0.2% | 2,430 | 3,234 | +804 🟩 | 17.8% | 20.2% | +2.4pp 🟩 |
| Puttalam `LK-6215` | Puttalam | 3.0% | 52,934 | 63,101 | +10,167 🟩 | 64.2% | 66.6% | +2.4pp 🟩 |
| Karaitivu `LK-5227` | Ampara | 0.4% | 6,760 | 8,285 | +1,525 🟩 | 40.1% | 42.5% | +2.4pp 🟩 |
| Kobeigane `LK-6139` | Kurunegala | 0.3% | 3,862 | 5,322 | +1,460 🟩 | 10.7% | 13.1% | +2.4pp 🟩 |
| Maritimepattu `LK-4415` | Mullaitivu | 0.1% | 1,766 | 3,092 | +1,326 🟩 | 6.1% | 8.4% | +2.3pp 🟩 |
| Navithanveli `LK-5216` | Ampara | 0.4% | 6,402 | 7,967 | +1,565 🟩 | 34.2% | 36.5% | +2.3pp 🟩 |
| Pathadumbara `LK-2112` | Kandy | 1.1% | 20,239 | 23,313 | +3,074 🟩 | 22.8% | 24.9% | +2.1pp 🟩 |
| Attanagalla `LK-1227` | Gampaha | 1.4% | 22,303 | 28,406 | +6,103 🟩 | 12.4% | 14.4% | +1.9pp 🟩 |
| Ukuwela `LK-2233` | Matale | 0.8% | 14,180 | 16,475 | +2,295 🟩 | 20.8% | 22.8% | +1.9pp 🟩 |
| Panduwasnuwara West `LK-6145` | Kurunegala | 0.5% | 8,452 | 10,464 | +2,012 🟩 | 12.8% | 14.7% | +1.9pp 🟩 |
| Welimada `LK-8130` | Badulla | 1.0% | 16,921 | 19,720 | +2,799 🟩 | 16.8% | 18.7% | +1.9pp 🟩 |
| Udunuwara `LK-2139` | Kandy | 1.5% | 27,186 | 31,951 | +4,765 🟩 | 24.5% | 26.4% | +1.9pp 🟩 |
| Mallawapitiya `LK-6157` | Kurunegala | 0.5% | 7,924 | 10,018 | +2,094 🟩 | 15.1% | 16.8% | +1.8pp 🟩 |
| Udapalatha `LK-2151` | Kandy | 1.2% | 20,784 | 25,206 | +4,422 🟩 | 22.7% | 24.4% | +1.8pp 🟩 |
| Town & Gravets `LK-5315` | Trincomalee | 0.8% | 13,501 | 15,605 | +2,104 🟩 | 13.8% | 15.6% | +1.7pp 🟩 |
| Kuchchaweli `LK-5306` | Trincomalee | 1.3% | 21,308 | 26,239 | +4,931 🟩 | 64.1% | 65.8% | +1.7pp 🟩 |
| Kelaniya `LK-1236` | Gampaha | 0.7% | 12,439 | 14,312 | +1,873 🟩 | 9.1% | 10.7% | +1.6pp 🟩 |
| Rideegama `LK-6163` | Kurunegala | 0.6% | 10,022 | 12,391 | +2,369 🟩 | 11.3% | 12.9% | +1.6pp 🟩 |
| Muthur `LK-5327` | Trincomalee | 2.2% | 35,088 | 45,658 | +10,570 🟩 | 62.0% | 63.5% | +1.5pp 🟩 |
| Medagama `LK-8209` | Monaragala | 0.3% | 4,939 | 6,827 | +1,888 🟩 | 13.8% | 15.3% | +1.5pp 🟩 |
| Nattandiya `LK-6242` | Puttalam | 0.4% | 6,609 | 7,939 | +1,330 🟩 | 10.6% | 12.1% | +1.5pp 🟩 |
| Poonakary `LK-4512` | Kilinochchi | 0.0% | 469 | 909 | +440 🟩 | 2.3% | 3.8% | +1.5pp 🟩 |
| Manmunai North `LK-5118` | Batticaloa | 0.3% | 4,585 | 6,424 | +1,839 🟩 | 5.3% | 6.8% | +1.4pp 🟩 |
| Kantale `LK-5321` | Trincomalee | 0.4% | 7,633 | 9,020 | +1,387 🟩 | 16.3% | 17.7% | +1.4pp 🟩 |
| Kinniya `LK-5324` | Trincomalee | 4.1% | 61,880 | 84,032 | +22,152 🟩 | 95.8% | 97.1% | +1.4pp 🟩 |
| Colombo `LK-1103` | Colombo | 6.1% | 135,000 | 125,890 | -9,110 🟥 | 41.8% | 43.1% | +1.3pp 🟩 |
| Ganga Ihala Korale `LK-2154` | Kandy | 0.2% | 3,779 | 4,795 | +1,016 🟩 | 6.8% | 8.1% | +1.3pp 🟩 |
| Haputale `LK-8139` | Badulla | 0.2% | 3,665 | 4,165 | +500 🟩 | 7.4% | 8.6% | +1.3pp 🟩 |
| Poojapitiya `LK-2106` | Kandy | 0.5% | 9,571 | 10,718 | +1,147 🟩 | 16.5% | 17.8% | +1.2pp 🟩 |
| Weligama `LK-3239` | Matara | 0.4% | 7,379 | 8,652 | +1,273 🟩 | 10.1% | 11.4% | +1.2pp 🟩 |
| Mawathagama `LK-6160` | Kurunegala | 0.4% | 7,199 | 8,803 | +1,604 🟩 | 11.2% | 12.4% | +1.2pp 🟩 |
| Udubaddawa `LK-6175` | Kurunegala | 0.3% | 5,412 | 6,270 | +858 🟩 | 10.4% | 11.5% | +1.2pp 🟩 |
| Wattala `LK-1218` | Gampaha | 0.7% | 11,407 | 13,918 | +2,511 🟩 | 6.5% | 7.6% | +1.1pp 🟩 |
| Pannala `LK-6178` | Kurunegala | 0.5% | 7,205 | 9,398 | +2,193 🟩 | 5.8% | 6.9% | +1.1pp 🟩 |
| Koralai Pattu North `LK-5103` | Batticaloa | 0.1% | 699 | 1,095 | +396 🟩 | 3.2% | 4.3% | +1.1pp 🟩 |
| Thimbirigasyaya `LK-1127` | Colombo | 1.9% | 41,447 | 40,132 | -1,315 🟥 | 17.4% | 18.5% | +1.1pp 🟩 |
| Rambewa `LK-7118` | Anuradhapura | 0.3% | 5,683 | 5,242 | -441 🟥 | 15.5% | 13.2% | -2.3pp 🟥 |
| Koralai Pattu Central `LK-5104` | Batticaloa | 0.0% | 24,965 | 94 | -24,871 🟥 | 97.2% | 0.3% | -96.9pp 🟥 |

***Musali** gained the most share at **+15.1pp**. **Koralai Pattu Central** saw the steepest share decline at **-96.9pp**. **Kolonnawa** had the largest absolute increase (**+22,911**).*

### Roman Catholic

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Delft `LK-4142` | Jaffna | 0.2% | 2,077 | 1,924 | -153 🟥 | 54.3% | 60.9% | +6.6pp 🟩 |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu | 0.5% | 2,305 | 5,817 | +3,512 🟩 | 9.7% | 14.7% | +5.0pp 🟩 |
| Koralai Pattu Central `LK-5104` | Batticaloa | 0.1% | 63 | 1,257 | +1,194 🟩 | 0.2% | 4.4% | +4.1pp 🟩 |
| Islands South (Velanai) `LK-4139` | Jaffna | 0.4% | 3,619 | 4,263 | +644 🟩 | 21.6% | 25.7% | +4.1pp 🟩 |
| Nallur `LK-4133` | Jaffna | 0.4% | 3,453 | 5,310 | +1,857 🟩 | 5.1% | 7.3% | +2.2pp 🟩 |
| Katana `LK-1206` | Gampaha | 6.9% | 75,385 | 81,913 | +6,528 🟩 | 32.0% | 34.0% | +1.9pp 🟩 |
| Kalpitiya `LK-6203` | Puttalam | 2.8% | 27,880 | 32,625 | +4,745 🟩 | 32.3% | 33.6% | +1.4pp 🟩 |
| Poonakary `LK-4512` | Kilinochchi | 0.5% | 4,621 | 5,767 | +1,146 🟩 | 22.8% | 23.9% | +1.2pp 🟩 |
| Islands North (Kayts) `LK-4103` | Jaffna | 0.4% | 4,062 | 4,196 | +134 🟩 | 41.1% | 42.3% | +1.1pp 🟩 |
| Valikamam North (Thllippalai) `LK-4112` | Jaffna | 0.4% | 2,866 | 4,843 | +1,977 🟩 | 9.7% | 10.8% | +1.1pp 🟩 |
| Vavuniya North `LK-4303` | Vavuniya | 0.0% | 313 | 555 | +242 🟩 | 2.7% | 3.8% | +1.1pp 🟩 |
| Gampaha `LK-1224` | Gampaha | 1.7% | 21,085 | 19,706 | -1,379 🟥 | 10.7% | 9.6% | -1.1pp 🟥 |
| Biyagama `LK-1239` | Gampaha | 0.6% | 8,533 | 7,229 | -1,304 🟥 | 4.6% | 3.5% | -1.1pp 🟥 |
| Gangawata Korale `LK-2130` | Kandy | 0.5% | 7,557 | 5,616 | -1,941 🟥 | 4.8% | 3.7% | -1.1pp 🟥 |
| Maritimepattu `LK-4415` | Mullaitivu | 0.5% | 5,293 | 6,329 | +1,036 🟩 | 18.3% | 17.2% | -1.1pp 🟥 |
| Mundel `LK-6218` | Puttalam | 1.7% | 17,806 | 20,129 | +2,323 🟩 | 28.9% | 27.7% | -1.2pp 🟥 |
| Kaduwela `LK-1109` | Colombo | 0.9% | 12,519 | 10,576 | -1,943 🟥 | 5.0% | 3.8% | -1.2pp 🟥 |
| Bingiriya `LK-6142` | Kurunegala | 0.5% | 6,401 | 6,072 | -329 🟥 | 10.3% | 9.1% | -1.2pp 🟥 |
| Mahara `LK-1233` | Gampaha | 1.4% | 18,183 | 16,909 | -1,274 🟥 | 8.8% | 7.6% | -1.2pp 🟥 |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.1% | 942 | 1,280 | +338 🟩 | 11.0% | 9.8% | -1.2pp 🟥 |
| Chilaw `LK-6233` | Puttalam | 2.4% | 28,544 | 28,248 | -296 🟥 | 45.7% | 44.4% | -1.3pp 🟥 |
| Madampe `LK-6236` | Puttalam | 0.7% | 8,304 | 7,860 | -444 🟥 | 17.3% | 16.0% | -1.3pp 🟥 |
| Ratmalana `LK-1131` | Colombo | 0.5% | 7,183 | 5,455 | -1,728 🟥 | 7.5% | 6.2% | -1.3pp 🟥 |
| Mahawewa `LK-6239` | Puttalam | 2.1% | 26,436 | 24,602 | -1,834 🟥 | 51.8% | 50.4% | -1.4pp 🟥 |
| Seethawaka `LK-1115` | Colombo | 0.6% | 8,309 | 7,214 | -1,095 🟥 | 7.3% | 5.9% | -1.4pp 🟥 |
| Puttalam `LK-6215` | Puttalam | 0.7% | 8,302 | 8,222 | -80 🟥 | 10.1% | 8.7% | -1.4pp 🟥 |
| Manmunai North `LK-5118` | Batticaloa | 1.4% | 16,360 | 16,570 | +210 🟩 | 19.0% | 17.4% | -1.6pp 🟥 |
| Pallama `LK-6227` | Puttalam | 0.3% | 3,244 | 3,267 | +23 🟩 | 13.3% | 11.7% | -1.6pp 🟥 |
| Dehiwala `LK-1130` | Colombo | 0.4% | 5,976 | 4,627 | -1,349 🟥 | 6.7% | 4.9% | -1.8pp 🟥 |
| Negombo `LK-1203` | Gampaha | 7.4% | 92,828 | 87,605 | -5,223 🟥 | 65.3% | 63.5% | -1.8pp 🟥 |
| Dankotuwa `LK-6248` | Puttalam | 1.5% | 18,622 | 17,539 | -1,083 🟥 | 29.8% | 27.9% | -1.9pp 🟥 |
| Nanaddan `LK-4212` | Mannar | 1.1% | 12,229 | 13,056 | +827 🟩 | 68.4% | 66.4% | -2.0pp 🟥 |
| Udubaddawa `LK-6175` | Kurunegala | 0.6% | 7,506 | 6,724 | -782 🟥 | 14.4% | 12.3% | -2.0pp 🟥 |
| Kelaniya `LK-1236` | Gampaha | 0.9% | 13,458 | 10,341 | -3,117 🟥 | 9.8% | 7.7% | -2.1pp 🟥 |
| Karuwalagaswewa `LK-6209` | Puttalam | 0.1% | 1,791 | 1,447 | -344 🟥 | 7.6% | 5.5% | -2.1pp 🟥 |
| Jaffna `LK-4136` | Jaffna | 2.1% | 26,700 | 24,546 | -2,154 🟥 | 52.9% | 50.6% | -2.3pp 🟥 |
| Vadamaradchi North (Point Pedro) `LK-4127` | Jaffna | 0.4% | 6,356 | 4,781 | -1,575 🟥 | 13.4% | 11.0% | -2.3pp 🟥 |
| Nattandiya `LK-6242` | Puttalam | 2.1% | 25,226 | 25,002 | -224 🟥 | 40.6% | 38.2% | -2.4pp 🟥 |
| Wattala `LK-1218` | Gampaha | 6.5% | 79,334 | 77,121 | -2,213 🟥 | 45.2% | 42.3% | -2.9pp 🟥 |
| Madhu `LK-4209` | Mannar | 0.3% | 2,997 | 3,319 | +322 🟩 | 38.9% | 35.0% | -3.9pp 🟥 |
| Mannar Town `LK-4203` | Mannar | 2.5% | 27,970 | 29,246 | +1,276 🟩 | 54.8% | 50.6% | -4.1pp 🟥 |
| Vengalacheddikulam `LK-4312` | Vavuniya | 0.2% | 4,564 | 2,821 | -1,743 🟥 | 15.3% | 10.9% | -4.3pp 🟥 |
| Musali `LK-4215` | Mannar | 0.3% | 2,750 | 4,011 | +1,261 🟩 | 33.9% | 22.1% | -11.8pp 🟥 |

***Delft** gained the most share at **+6.6pp**. **Musali** saw the steepest share decline at **-11.8pp**. **Katana** had the largest absolute increase (**+6,528**).*

### Other Christian

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Koralai Pattu Central `LK-5104` | Batticaloa | 1.4% | 12 | 3,459 | +3,447 🟩 | 0.0% | 12.0% | +12.0pp 🟩 |
| Koralai Pattu South `LK-5110` | Batticaloa | 0.9% | 1,471 | 2,244 | +773 🟩 | 5.6% | 7.9% | +2.3pp 🟩 |
| Thunukkai `LK-4403` | Mullaitivu | 0.2% | 382 | 584 | +202 🟩 | 3.9% | 5.6% | +1.7pp 🟩 |
| Pachchilaipalli `LK-4503` | Kilinochchi | 0.2% | 162 | 461 | +299 🟩 | 1.9% | 3.5% | +1.6pp 🟩 |
| Islands North (Kayts) `LK-4103` | Jaffna | 0.2% | 387 | 543 | +156 🟩 | 3.9% | 5.5% | +1.5pp 🟩 |
| Vavuniya South `LK-4306` | Vavuniya | 0.1% | 45 | 265 | +220 🟩 | 0.3% | 1.8% | +1.4pp 🟩 |
| Koralai Pattu North `LK-5103` | Batticaloa | 1.3% | 2,597 | 3,432 | +835 🟩 | 12.1% | 13.5% | +1.4pp 🟩 |
| Oddusuddan `LK-4412` | Mullaitivu | 0.5% | 877 | 1,267 | +390 🟩 | 5.6% | 7.0% | +1.4pp 🟩 |
| Maritimepattu `LK-4415` | Mullaitivu | 0.6% | 838 | 1,510 | +672 🟩 | 2.9% | 4.1% | +1.2pp 🟩 |
| Puthukkudiyiruppu `LK-4409` | Mullaitivu | 1.0% | 1,239 | 2,530 | +1,291 🟩 | 5.2% | 6.4% | +1.2pp 🟩 |
| Valikamam North (Thllippalai) `LK-4112` | Jaffna | 0.7% | 869 | 1,857 | +988 🟩 | 2.9% | 4.1% | +1.2pp 🟩 |
| Thimbirigasyaya `LK-1127` | Colombo | 2.8% | 10,262 | 7,036 | -3,226 🟥 | 4.3% | 3.2% | -1.1pp 🟥 |
| Manmunai South & Eruvil Pattu `LK-5136` | Batticaloa | 0.5% | 1,836 | 1,216 | -620 🟥 | 3.0% | 1.9% | -1.1pp 🟥 |
| Sri Jayawardanapura Kotte `LK-1124` | Colombo | 1.3% | 5,055 | 3,379 | -1,676 🟥 | 4.7% | 3.5% | -1.2pp 🟥 |
| Dehiwala `LK-1130` | Colombo | 1.0% | 3,684 | 2,557 | -1,127 🟥 | 4.1% | 2.7% | -1.4pp 🟥 |

***Koralai Pattu Central** gained the most share at **+12.0pp**. **Dehiwala** saw the steepest share decline at **-1.4pp**.*

### Other

| DSD | District | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Kalpitiya `LK-6203` | Puttalam | 0.2% | 1,045 | 9 | -1,036 🟥 | 1.2% | 0.0% | -1.2pp 🟥 |

***Kalpitiya** saw the steepest share decline at **-1.2pp**.*

---

## A8. Religion by Country: Key Trends

![A8 country share change](analyses/a8_by_country/chart.png)

This mirrors A2 at country scope, treating **Sri Lanka** as a single region.

Tables list only rows where absolute share change is **> 1.0pp**.

### Buddhist

| Country | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|

*No regions exceed the table share-change threshold.*

### Hindu

| Country | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|

*No regions exceed the table share-change threshold.*

### Islam

| Country | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sri Lanka `LK` | 100.0% | 1,967,008 | 2,337,379 | +370,371 🟩 | 9.7% | 10.7% | +1.1pp 🟩 |

* **Sri Lanka** gained share at **+1.1pp**.*

### Roman Catholic

| Country | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|

*No regions exceed the table share-change threshold.*

### Other Christian

| Country | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|

*No regions exceed the table share-change threshold.*

### Other

| Country | % Nationally | 2012 | 2024 | Change | % of Population (2012) | % of Population (2024) | Change in % of Population (pp) |
|---|---:|---:|---:|---:|---:|---:|---:|

*No regions exceed the table share-change threshold.*

---

*Data from the 2012 and 2024 Sri Lanka Census, accessed via [lanka_data](https://pypi.org/project/lanka-data/). Raw data and derived tables live in the corresponding directories under [`analyses/`](analyses/).*
