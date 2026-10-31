# Nested Loop Examination Seating Generator Using Python

## 1. Problem Statement

Write a Python program to generate an examination seating arrangement using nested loops. The program should arrange students in rows and columns based on the fixed classroom capacity.

The program must perform the following operations:

1. Accept the number of rows and columns in the classroom.
2. Generate unique row and column identifiers for each seat.
3. Mark specified seats as reserved.
4. Apply alternate seating restrictions to maintain distance between students.
5. Ensure that the seating arrangement does not exceed the fixed classroom capacity.
6. Display the final seating arrangement in a tabular format.

Seating rules:

- Each seat must have a unique row and column identifier.
- Reserved seats must be marked as `R`.
- Alternate seating positions must be marked as `X` (not available).
- Available examination seats must be marked as `S`.
- The total number of seats must not exceed classroom capacity.

## 2. Algorithm

1. Start the program.
2. Read the number of rows and columns.
3. Read the maximum classroom capacity.
4. Calculate the total number of seats.
5. Check whether the total seats exceed classroom capacity.
   - If yes, display an error message.
   - Otherwise, continue.
6. Read the number of reserved seats.
7. Accept the row and column positions of reserved seats.
8. Initialize the seating arrangement.
9. Use nested loops:
   - Outer loop represents rows.
   - Inner loop represents columns.
10. For each position:
    - If the position is reserved, mark it as `R`.
    - Else if the position follows the alternate seating restriction, mark it as `X`.
    - Otherwise, mark it as `S`.
11. Display the seating arrangement with row and column identifiers.
12. Count and display the available seats.
13. Stop the program.


## 4. Python Source Code

```

flowchart TD
    A([Start]) --> B[/Input Rows and Columns/]
    B --> C[/Input Classroom Capacity/]
    C --> D[Calculate Total Seats]
    D --> E{Total Seats <= Capacity?}

    E -- No --> F[Display Capacity Error]
    F --> Z([Stop])

    E -- Yes --> G[/Input Reserved Seat Positions/]
    G --> H[Initialize Counters]
    H --> I[Start Outer Loop for Rows]
    I --> J[Start Inner Loop for Columns]

    J --> K{Seat Reserved?}
    K -- Yes --> L[Mark Seat as R]
    K -- No --> M{Alternate Restriction?}

    M -- Yes --> N[Mark Seat as X]
    M -- No --> O[Mark Seat as S]

    L --> P[Update Seat Counters]
    N --> P
    O --> P

    P --> Q{More Columns?}
    Q -- Yes --> J
    Q -- No --> R{More Rows?}

    R -- Yes --> I
    R -- No --> S[Display Seating Arrangement]

    S --> T[Display Seating Summary]
    T --> Z([Stop])
            
```

## 5. Sample Input

```
Enter number of rows: 4
Enter number of columns: 4
Enter classroom capacity: 20
Enter number of reserved seats: 2

Enter reserved seat positions (row column):
1 2
3 4
```

## 6. Sample Output

```
EXAMINATION SEATING ARRANGEMENT

Row 1 : [1-1:X] [1-2:R] [1-3:X] [1-4:S]
Row 2 : [2-1:S] [2-2:X] [2-3:S] [2-4:X]
Row 3 : [3-1:X] [3-2:S] [3-3:X] [3-4:R]
Row 4 : [4-1:S] [4-2:X] [4-3:S] [4-4:X]

========== SEATING SUMMARY ==========
Total Classroom Seats : 16
Reserved Seats        : 2
Restricted Seats      : 7
Available Seats       : 7
Classroom Capacity    : 20
=====================================
```

## 7. Mermaid Flowchart Code

Copy the following code into the [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate the flowchart.

\#chatgpt-mermaid-\_r_dl\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_dl\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_dl\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_dl\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_dl\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dl\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_dl\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_dl\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_dl\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_dl\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_dl\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_dl\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dl\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dl\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_dl\_ p{margin:0;}#chatgpt-mermaid-\_r_dl\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dl\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dl\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dl\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_dl\_ .label text,#chatgpt-mermaid-\_r_dl\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dl\_ .node rect,#chatgpt-mermaid-\_r_dl\_ .node circle,#chatgpt-mermaid-\_r_dl\_ .node ellipse,#chatgpt-mermaid-\_r_dl\_ .node polygon,#chatgpt-mermaid-\_r_dl\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_dl\_ .rough-node .label text,#chatgpt-mermaid-\_r_dl\_ .node .label text,#chatgpt-mermaid-\_r_dl\_ .image-shape .label,#chatgpt-mermaid-\_r_dl\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_dl\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_dl\_ .rough-node .label,#chatgpt-mermaid-\_r_dl\_ .node .label,#chatgpt-mermaid-\_r_dl\_ .image-shape .label,#chatgpt-mermaid-\_r_dl\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_dl\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_dl\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dl\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dl\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_dl\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_dl\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_dl\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_dl\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_dl\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_dl\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_dl\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dl\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dl\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_dl\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dl\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_dl\_ .icon-shape,#chatgpt-mermaid-\_r_dl\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_dl\_ .icon-shape p,#chatgpt-mermaid-\_r_dl\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_dl\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_dl\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_dl\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_dl\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_dl\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_dl\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_dl\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_dl\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_dl\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dl\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_dl\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dl\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_dl\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_dl\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_dl\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_dl\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_dl\_ .node rect,#chatgpt-mermaid-\_r_dl\_ .node circle,#chatgpt-mermaid-\_r_dl\_ .node ellipse,#chatgpt-mermaid-\_r_dl\_ .node polygon,#chatgpt-mermaid-\_r_dl\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_dl\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_dl\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_dl\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_dl\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dl\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput Rows and ColumnsInput Classroom CapacityCalculate Total SeatsTotal Seats <= Capacity?Display Capacity ErrorStopInput Reserved Seat PositionsInitialize CountersStart Outer Loop for RowsStart Inner Loop for ColumnsSeat Reserved?Mark Seat as RAlternate Restriction?Mark Seat as XMark Seat as SUpdate Seat CountersMore Columns?More Rows?Display Seating ArrangementDisplay Seating SummaryNoYesYesNoYesNoYesNoYesNo

## 8. Expected Result

The Python program generates an examination seating arrangement using nested loops. It assigns unique row and column identifiers, marks reserved seats, applies alternate seating restrictions, and checks the classroom capacity.

The program displays the final seating layout along with the total number of reserved, restricted, and available seats.

Seat identification:

| Symbol | Meaning         |
| ------ | --------------- |
| S      | Available seat  |
| R      | Reserved seat   |
| X      | Restricted seat |

Note: Alternate seating is implemented using the condition `(row + column) % 2 == 0`. This creates a checkerboard-style restriction pattern. Reserved seats take priority over alternate seating restrictions.
