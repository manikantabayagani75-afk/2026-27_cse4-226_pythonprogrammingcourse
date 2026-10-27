**# University Scholarship Allocation System – Python Program

## 1. Problem Statement

Design a University Scholarship Allocation System that evaluates student applications based on aggregate marks, subject-wise minimum marks, attendance percentage, and annual family income.

The system should:

- Check whether each applicant satisfies all eligibility criteria.
- Reject applicants who fail any mandatory condition and display the reason.
- Rank eligible applicants based on aggregate marks.
- Resolve ties using predefined rules:
  1. Higher aggregate marks.
  2. Higher priority-subject marks.
  3. Higher attendance percentage.
  4. Lower annual family income.
- Allocate scholarships to the top-ranked eligible students according to the available quota.

Assumed eligibility criteria:

- Aggregate marks ≥ 75%.
- Every subject mark ≥ 60%.
- Attendance ≥ 75%.
- Annual family income ≤ ₹2,50,000.
- Scholarship quota = 3 students.

## 2. Algorithm

1. Start.
2. Read the number of applicants and scholarship quota.
3. For each applicant, input their ID, name, subject marks, attendance, and annual family income.
4. Calculate aggregate percentage from the subject marks.
5. Validate the input data.
6. Check all eligibility conditions.
7. If any condition fails, mark the applicant as ineligible and record the reason.
8. Otherwise, add the applicant to the eligible list.
9. Sort eligible applicants using the following priorities:
   - Aggregate marks in descending order.
   - Priority-subject total in descending order.
   - Attendance in descending order.
   - Annual family income in ascending order.
   - Application ID in ascending order for deterministic ordering.
10. Allocate scholarships to the top-ranked students up to the quota.
11. Display the ranked list, rejected applicants, and scholarship awardees.
12. Stop.

## 3. Flowchart
...

flowchart TD
    A([Start]) --> B[/Input applicant details and quota/]
    B --> C[Calculate aggregate marks]
    C --> D{Are all inputs valid?}

    D -- No --> E[Record invalid application]
    D -- Yes --> F{Meet all eligibility criteria?}

    F -- No --> G[Record rejection reasons]
    F -- Yes --> H[Add applicant to eligible list]

    E --> I{More applicants?}
    G --> I
    H --> I

    I -- Yes --> B
    I -- No --> J[Sort eligible applicants]

    J --> K[Apply tie-breaking rules]
    K --> L[Select top applicants up to quota]
    L --> M[/Display ranking and awardees/]
    M --> N([Stop])

    style A fill:#d5f5e3,stroke:#229954
    style N fill:#d5f5e3,stroke:#229954
    style F fill:#fcf3cf,stroke:#b7950b
    style D fill:#fcf3cf,stroke:#b7950b

```

## 5. Sample Input

The following input represents five applicants. In the source code above, the sample data is already initialized, so no keyboard input is required.

text

```
Scholarship quota: 3

ID     Name     Subject Marks     Attendance   Annual Income
A101   Ananya   90 85 88          95%          180000
A102   Bharat   85 85 85          90%          120000
A103   Charan   78 80 76          85%          200000
A104   Divya    92 55 90          98%          100000
A105   Esha     85 85 85          95%          150000
```

## 6. Sample Output

text

```
UNIVERSITY SCHOLARSHIP ALLOCATION
------------------------------------------------------------

RANKED ELIGIBLE APPLICANTS
1. A101 - Ananya | Aggregate: 87.67% | Attendance: 95%
2. A105 - Esha | Aggregate: 85.00% | Attendance: 95%
3. A102 - Bharat | Aggregate: 85.00% | Attendance: 90%
4. A103 - Charan | Aggregate: 78.00% | Attendance: 85%

INELIGIBLE APPLICANTS
A104 - Divya
  - Subject marks below 60%

SCHOLARSHIP AWARDEES
1. A101 - Ananya | Aggregate: 87.67%
2. A105 - Esha | Aggregate: 85.00%
3. A102 - Bharat | Aggregate: 85.00%
```

Explanation: Esha ranks above Bharat because they have the same aggregate marks and priority-subject total, but Esha has higher attendance. Divya is rejected because one subject mark is below the required minimum, even though her aggregate exceeds 75%.

## 7. Mermaid Flowchart Code

Copy this code into the [Mermaid Live Editor](<https://mermaid.live/?utm_source=chatgpt.com>) to render or export the flowchart.

mermaid

```

flowchart TD
    A([Start]) --> B[/Input applicant details and quota/]
    B --> C[Calculate aggregate marks]
    C --> D{Are all inputs valid?}

    D -- No --> E[Record invalid application]
    D -- Yes --> F{Meet all eligibility criteria?}

    F -- No --> G[Record rejection reasons]
    F -- Yes --> H[Add applicant to eligible list]

    E --> I{More applicants?}
    G --> I
    H --> I

    I -- Yes --> B
    I -- No --> J[Sort eligible applicants]

    J --> K[Apply tie-breaking rules]
    K --> L[Select top applicants up to quota]
    L --> M[/Display ranking and awardees/]
    M --> N([Stop])

    style A fill:#d5f5e3,stroke:#229954
    style N fill:#d5f5e3,stroke:#229954
    style F fill:#fcf3cf,stroke:#b7950b
    style D fill:#fcf3cf,stroke:#b7950b
```

## 8. Result

The system successfully evaluates scholarship applicants, checks all mandatory conditions, ranks eligible students, resolves ties using predefined criteria, and allocates scholarships according to the available quota.

Time complexity: $O(n \log n)$ for sorting $n$ eligible applicants, excluding the linear eligibility checks.**
