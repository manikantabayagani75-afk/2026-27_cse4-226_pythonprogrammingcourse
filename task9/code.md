# Text-Based Invoice Data Extraction Using Python

## 1. Problem Statement

Write a Python program to perform text-based invoice data extraction using basic string operations.

The program should process formatted invoice records and extract important details such as:

- Product code
- Product quantity
- Product amount

The program should validate each invoice record and identify malformed records that do not follow the required format.

The program must:

1. Accept invoice records as formatted strings.
2. Split each record using a delimiter.
3. Extract product code, quantity, and amount.
4. Validate the extracted data.
5. Flag malformed records.
6. Display valid invoice details and the total invoice amount.

Input format:

```
ProductCode,Quantity,Amount
```

Example:

```
P101,2,500
```

## 2. Algorithm

1. Start the program.
2. Initialize the total invoice amount to zero.
3. Read the number of invoice records.
4. Repeat for each invoice record:
   - Read the invoice string.
   - Split the string using a comma delimiter.
   - Check whether the record contains exactly three fields.
   - Extract product code, quantity, and amount.
   - Check whether the product code is not empty.
   - Check whether quantity is a positive integer.
   - Check whether amount is a positive number.
   - If all conditions are satisfied:
     - Display the extracted product details.
     - Add the amount to the total invoice amount.
     - Increment the valid record count.
   - Otherwise:
     - Display a malformed record message.
     - Increment the invalid record count.
5. Display the total invoice amount.
6. Display the number of valid and malformed records.
7. Stop the program.


## 4. Python Source Code

```
 
flowchart TD
    A([Start]) --> B[Initialize Total Amount = 0]
    B --> C[Initialize Valid and Invalid Counters]
    C --> D[/Enter Number of Records/]
    D --> E[/Read Invoice Record/]
    E --> F[Split Record Using Comma]
    F --> G{Exactly 3 Fields?}

    G -- No --> H[Flag Malformed Record]
    G -- Yes --> I[Extract Code, Quantity and Amount]

    I --> J{Product Code Not Empty?}
    J -- No --> H
    J -- Yes --> K{Quantity and Amount Numeric?}

    K -- No --> H
    K -- Yes --> L{Quantity > 0 and Amount > 0?}

    L -- No --> H
    L -- Yes --> M[Display Valid Invoice Details]

    M --> N[Add Amount to Total]
    N --> O[Increment Valid Counter]

    H --> P[Increment Invalid Counter]
    O --> Q{More Records?}
    P --> Q

    Q -- Yes --> E
    Q -- No --> R[Display Invoice Summary]
    R --> S([Stop])

```

## 5. Sample Input

```
Enter number of invoice records: 5

P101,2,500
P102,3,750
P103,abc,600
P104,1,1200
P105,2
```

## 6. Sample Output

```
Enter number of invoice records: 5

Enter invoice record: P101,2,500

Valid Invoice Record
Product Code: P101
Quantity: 2
Amount: Rs. 500.0

Enter invoice record: P102,3,750

Valid Invoice Record
Product Code: P102
Quantity: 3
Amount: Rs. 750.0

Enter invoice record: P103,abc,600
Malformed Record: Invalid numeric values

Enter invoice record: P104,1,1200

Valid Invoice Record
Product Code: P104
Quantity: 1
Amount: Rs. 1200.0

Enter invoice record: P105,2
Malformed Record: Incorrect number of fields

========== INVOICE SUMMARY ==========
Valid Records: 3
Malformed Records: 2
Total Invoice Amount: Rs. 2450.0
=====================================
```

## 7. Mermaid Flowchart Code

Copy the following code into the [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate the flowchart.

\#chatgpt-mermaid-\_r_b3\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_b3\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_b3\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_b3\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_b3\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_b3\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_b3\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_b3\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_b3\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_b3\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_b3\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_b3\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_b3\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_b3\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_b3\_ p{margin:0;}#chatgpt-mermaid-\_r_b3\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_b3\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_b3\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_b3\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_b3\_ .label text,#chatgpt-mermaid-\_r_b3\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_b3\_ .node rect,#chatgpt-mermaid-\_r_b3\_ .node circle,#chatgpt-mermaid-\_r_b3\_ .node ellipse,#chatgpt-mermaid-\_r_b3\_ .node polygon,#chatgpt-mermaid-\_r_b3\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_b3\_ .rough-node .label text,#chatgpt-mermaid-\_r_b3\_ .node .label text,#chatgpt-mermaid-\_r_b3\_ .image-shape .label,#chatgpt-mermaid-\_r_b3\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_b3\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_b3\_ .rough-node .label,#chatgpt-mermaid-\_r_b3\_ .node .label,#chatgpt-mermaid-\_r_b3\_ .image-shape .label,#chatgpt-mermaid-\_r_b3\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_b3\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_b3\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_b3\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_b3\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_b3\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_b3\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_b3\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_b3\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_b3\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_b3\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_b3\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_b3\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_b3\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_b3\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_b3\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_b3\_ .icon-shape,#chatgpt-mermaid-\_r_b3\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_b3\_ .icon-shape p,#chatgpt-mermaid-\_r_b3\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_b3\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_b3\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_b3\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_b3\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_b3\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_b3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_b3\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_b3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_b3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b3\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_b3\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_b3\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_b3\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_b3\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_b3\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_b3\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_b3\_ .node rect,#chatgpt-mermaid-\_r_b3\_ .node circle,#chatgpt-mermaid-\_r_b3\_ .node ellipse,#chatgpt-mermaid-\_r_b3\_ .node polygon,#chatgpt-mermaid-\_r_b3\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_b3\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_b3\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_b3\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_b3\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_b3\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInitialize Total Amount = 0Initialize Valid and InvalidCountersEnter Number of RecordsRead Invoice RecordSplit Record Using CommaExactly 3 Fields?Flag Malformed RecordExtract Code, Quantity andAmountProduct Code Not Empty?Quantity and AmountNumeric?Quantity 0 and Amount 0?Display Valid Invoice DetailsAdd Amount to TotalIncrement Valid CounterIncrement Invalid CounterMore Records?Display Invoice SummaryStopNoYesNoYesNoYesNoYesYesNo

## 8. Expected Result

The program successfully extracts product codes, quantities, and amounts from formatted invoice strings using basic Python string operations.

It identifies malformed invoice records, validates numeric values, calculates the total invoice amount, and displays the number of valid and invalid records.

Note: This program assumes that each record follows the format `ProductCode,Quantity,Amount`. The amount is treated as the total amount for that product record, not the per-unit price.
