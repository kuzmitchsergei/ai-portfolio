# Sergei Kuzmitch · AI portfolio

Key account manager learning to build practical AI tools. Based in Zurich.

For 12 years I managed key accounts for capital equipment in the security printing industry: central banks and state printing works in more than 20 countries, around ten tenders a year from CHF 150K to CHF 7M, and the service business behind them. I hold a Dipl.-Ing. in Electrical Power Engineering, an Executive MBA from ESCP Business School and the PMP certification.

## What I'm building, and why

Most AI demos are built by engineers, for engineers. I'm building tools for the problems I worked on every day: supplier quotations, tenders, service requests and account research.

My rule for every tool: plain, checkable code does the arithmetic and the decisions, and the AI only does what it's good at, which is reading documents and writing text. A tool a buyer or a service manager can't trust is a tool nobody uses.

I started programming in Python in October 2026 and will begin the CAS ETH in AI, Data and Machine Learning in February 2027. This repository documents that path in public.

## Projects

### [Quote Check](https://github.com/kuzmitchsergei/quote-tool): supplier quotation analysis

Quote Check reads a supplier's spare-parts quotation, compares every line with the price history and market indices, and flags the increases that the supplier's stated reasons don't explain. It drafts a reply asking for justification, then reads the supplier's answer and checks each claim, for example whether a material-cost argument matches published commodity prices. Python does all the arithmetic; the AI only reads documents and drafts text, and guards stop it from inventing figures. Everything runs on a local model, so no quotation data leaves the computer. On a fictional test set with 16 planted price anomalies, it found all 16 with no false alarms.

### Coming next

- **Service manual assistant:** answers technician questions from equipment manuals, citing the page
- **Tender analyser:** turns a public tender into a compliance matrix with risks flagged
- **Service ticket triage:** classifies and routes service requests, with a human approving every reply

## Learning log

| Where | What |
| --- | --- |
| `py4e/` | Exercises from *Python for Everybody*, typed and tested by hand |
| `first_call.py` | My first call to the Claude API |
| `hello.py` | Where it started |

## How I work with AI

I use Claude as a pair programmer and tutor. I define the problem, design what the AI may and may not do, and test every step against cases from my own industry experience. The course exercises in `py4e/` I write myself, to learn the language properly.

## Contact

[LinkedIn](https://www.linkedin.com/in/sergeikuzmitch)
