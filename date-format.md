/ [Home](index.md)

## Date Format

Date formats are one of the most persistent interoperability failures in global communication—especially in North America.

---

## Sample Dates (Ambiguous Examples)

```
25.01.26
02.02.26
07.02.26
```

Likely intended meaning:

> **DD.MM.YY**
- 25 January 2026  
- 2 February 2026  
- 7 February 2026  

---

## Why This Breaks in North America

In North America, the default mental model is:

> **MM/DD/YY**

This creates ambiguity:

- `02.02.26` → Feb 2 **or** 2 Feb?
- `07.02.26` → July 2 **or** 7 Feb?
- `25.01.26` → Invalid → forces reinterpretation

Once a date requires interpretation, it has already failed.

---

## The Root Cause

North America uses:

> **MM/DD/YYYY**

This format is:
- Not logical
- Not sortable
- Not internationally compatible
- A historical artifact, not a designed standard

It conflicts with:
- Europe → **DD/MM/YYYY**
- Asia → often **YYYY/MM/DD**
- Global software standards

---

## The Global Single Date Format (Correct Answer)

### ISO 8601 Standard

**Format:**
```
YYYY-MM-DD
```

**Examples:**
```
2026-01-25
2026-02-02
2026-02-07
```

---

## Why ISO 8601 Wins

| Property | ISO 8601 |
|--------|----------|
| Unambiguous | ✅ |
| Lexicographically sortable | ✅ |
| Human readable | ✅ |
| Machine friendly | ✅ |
| Timezone compatible | ✅ |
| Used in APIs & databases | ✅ |

This is why databases, APIs, logs, filenames, and distributed systems default to ISO 8601.

---

## Why People Still Don’t Use It

1. **Cultural inertia**
2. **Legacy systems**
3. **Familiarity beats correctness**

---

## What You Should Do (Best Practice)

### For professional, global, or technical communication
Always write:
```
2026-02-07
```


### For informal human communication
Spell the month:
```
7 Feb 2026
```

---

## Formats to Avoid Forever

- `25.01.26`
- `02/02/26`
- `07-02-26`
- Any **two-digit year**

---

## Engineering Rule of Thumb

> If a date format can be misread, it is a **bad format**.

ISO 8601 exists because humans failed to coordinate on dates.

