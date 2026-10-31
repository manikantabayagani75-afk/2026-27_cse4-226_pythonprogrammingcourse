# ATM Transaction Sequence Simulation Using Python

## 1. Problem Statement

Write a Python program to simulate ATM transactions. The program should process a sequence of deposits and withdrawals while maintaining the current account balance.

The program must:

- Accept the initial account balance.
- Allow users to deposit money.
- Allow users to withdraw money.
- Enforce a maximum withdrawal limit per transaction.
- Reject invalid transactions, such as negative amounts, zero amounts, insufficient balance, or withdrawals exceeding the limit.
- Display the updated balance after each valid transaction.
- Generate a final transaction summary showing the total deposits, total withdrawals, successful transactions, rejected transactions, and final balance.

## 2. Algorithm

1. Start the program.
2. Read the initial account balance.
3. Initialize:
   - Total deposits = 0
   - Total withdrawals = 0
   - Successful transactions = 0
   - Rejected transactions = 0
4. Set the maximum withdrawal limit to ₹10,000.
5. Read the number of transactions.
6. Repeat for each transaction:
   - Read the transaction type.
   - Read the transaction amount.
   - If the amount is less than or equal to zero, reject the transaction.
   - If the transaction is a deposit:
     - Add the amount to the balance.
     - Update total deposits.
   - If the transaction is a withdrawal:
     - Check whether the amount exceeds the withdrawal limit.
     - Check whether sufficient balance is available.
     - If both conditions are satisfied, subtract the amount from the balance.
     - Otherwise, reject the transaction.
   - If the transaction type is invalid, reject it.
   - Update transaction counters.
   - Display the transaction result and current balance.
7. Display the final transaction summary.
8. Stop the program.


## 4. Python Source Code

```

flowchart TD
    A([Start]) --> B[/Enter Initial Balance/]
    B --> C[Initialize Counters and Limit]
    C --> D[/Enter Number of Transactions/]
    D --> E[Read Transaction Type and Amount]

    E --> F{Amount > 0?}

    F -- No --> G[Reject Invalid Amount]
    F -- Yes --> H{Transaction Type?}

    H -- Deposit --> I[Add Amount to Balance]
    I --> J[Update Total Deposits]
    J --> K[Increment Successful Count]

    H -- Withdrawal --> L{Amount <= Withdrawal Limit?}
    L -- No --> M[Reject: Limit Exceeded]
    L -- Yes --> N{Sufficient Balance?}

    N -- No --> O[Reject: Insufficient Balance]
    N -- Yes --> P[Subtract Amount from Balance]
    P --> Q[Update Total Withdrawals]
    Q --> K

    H -- Invalid --> R[Reject Invalid Transaction]

    G --> S[Increment Rejected Count]
    M --> S
    O --> S
    R --> S

    K --> T[Display Current Balance]
    S --> T

    T --> U{More Transactions?}
    U -- Yes --> E
    U -- No --> V[Display Transaction Summary]
    V --> W([Stop])

```

## 5. Sample Input

```
Enter initial balance: Rs. 15000
Enter number of transactions: 5

Transaction 1
D
5000

Transaction 2
W
3000

Transaction 3
W
12000

Transaction 4
W
2000

Transaction 5
D
1000
```

## 6. Sample Output

```
Transaction 1
Deposit successful!
Current Balance: Rs. 20000.0

Transaction 2
Withdrawal successful!
Current Balance: Rs. 17000.0

Transaction 3
Rejected: Withdrawal limit exceeded
Current Balance: Rs. 17000.0

Transaction 4
Withdrawal successful!
Current Balance: Rs. 15000.0

Transaction 5
Deposit successful!
Current Balance: Rs. 16000.0

========== ATM TRANSACTION SUMMARY ==========
Total Deposits       : Rs. 6000.0
Total Withdrawals    : Rs. 5000.0
Successful Transactions: 4
Rejected Transactions  : 1
Final Account Balance  : Rs. 16000.0
============================================
```

## 7. Mermaid Flowchart Code

You can copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate the flowchart.

\#chatgpt-mermaid-\_r_8a\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_8a\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_8a\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_8a\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_8a\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_8a\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_8a\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_8a\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_8a\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_8a\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_8a\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_8a\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_8a\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_8a\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_8a\_ p{margin:0;}#chatgpt-mermaid-\_r_8a\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_8a\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_8a\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_8a\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_8a\_ .label text,#chatgpt-mermaid-\_r_8a\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_8a\_ .node rect,#chatgpt-mermaid-\_r_8a\_ .node circle,#chatgpt-mermaid-\_r_8a\_ .node ellipse,#chatgpt-mermaid-\_r_8a\_ .node polygon,#chatgpt-mermaid-\_r_8a\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_8a\_ .rough-node .label text,#chatgpt-mermaid-\_r_8a\_ .node .label text,#chatgpt-mermaid-\_r_8a\_ .image-shape .label,#chatgpt-mermaid-\_r_8a\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_8a\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_8a\_ .rough-node .label,#chatgpt-mermaid-\_r_8a\_ .node .label,#chatgpt-mermaid-\_r_8a\_ .image-shape .label,#chatgpt-mermaid-\_r_8a\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_8a\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_8a\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_8a\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_8a\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_8a\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_8a\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_8a\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_8a\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_8a\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_8a\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_8a\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_8a\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_8a\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_8a\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_8a\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_8a\_ .icon-shape,#chatgpt-mermaid-\_r_8a\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_8a\_ .icon-shape p,#chatgpt-mermaid-\_r_8a\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_8a\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_8a\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_8a\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_8a\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_8a\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_8a\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_8a\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_8a\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_8a\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_8a\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_8a\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_8a\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_8a\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_8a\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_8a\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_8a\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_8a\_ .node rect,#chatgpt-mermaid-\_r_8a\_ .node circle,#chatgpt-mermaid-\_r_8a\_ .node ellipse,#chatgpt-mermaid-\_r_8a\_ .node polygon,#chatgpt-mermaid-\_r_8a\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_8a\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_8a\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_8a\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_8a\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_8a\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter Initial BalanceInitialize Counters and LimitEnter Number of TransactionsRead Transaction Type andAmountAmount 0?Reject Invalid AmountTransaction Type?Add Amount to BalanceUpdate Total DepositsIncrement Successful CountAmount <= Withdrawal Limit?Reject: Limit ExceededSufficient Balance?Reject: Insufficient BalanceSubtract Amount from BalanceUpdate Total WithdrawalsReject Invalid TransactionIncrement Rejected CountDisplay Current BalanceMore Transactions?Display Transaction SummaryStopNoYesDepositWithdrawalNoYesNoYesInvalidYesNo

## 8. Expected Result

The Python program successfully simulates ATM deposit and withdrawal transactions. It maintains the account balance, enforces the withdrawal limit, rejects invalid transactions, and displays a summary of all successful and rejected transactions.

Note: The maximum withdrawal limit in this program is ₹10,000 per transaction. This is a simulation for educational purposes, not a real banking application.
