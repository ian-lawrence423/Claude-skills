import os, json
from datetime import datetime, timezone

skills_dir = r'C:\Users\IanLawrence\.claude\skills'
repo_dir = r'C:\Users\IanLawrence\github\Claude-skills'

skills = {
    'analytical-operating-system': ('Analytical Operating System', 'Universal investment analysis framework: thesis-first reasoning, MECE structure, Bayesian updating, evidence standards [F/E/H], and action bias.', 'analysis'),
    'deal-master': ('Deal Master', 'Single entry point for all deal intelligence. Inventories existing research, loads context, and routes to the right phase.', 'deal-intelligence'),
    'boundability': ('Boundability', 'Assess which investment risks are bounded, partially bounded, or unbounded. Two-layer framework: driver tree tiers + six-module issue assessment.', 'deal-intelligence'),
    'claim-scrutinizer': ('Claim Scrutinizer', 'Analyzes investment memos for structural gaps, unsupported claims, and logic errors. Seven-part test per material claim.', 'deal-intelligence'),
    'competitive-landscape-deliverable': ('Competitive Landscape Deliverable', 'Transforms a competitor spreadsheet into a formatted competitive landscape deliverable.', 'deal-intelligence'),
    'competitive-moat-assessment': ('Competitive Moat Assessment', 'Build a rigorous moat verdict per named competitor. Five moat types, existence-to-durability framework.', 'deal-intelligence'),
    'diligence-ddr': ('Diligence DDR', 'Generate a comprehensive Data Room Request tailored to the company and deal context.', 'deal-intelligence'),
    'doc-quality-checker': ('Doc Quality Checker', 'Quality and formatting check on Pattern-branded documents. Flags CRITICAL issues before distribution.', 'deal-intelligence'),
    'driver-tree': ('Driver Tree', 'Decomposes investment theses into MECE causal trees mapped to NTBs and MOIC.', 'deal-intelligence'),
    'executive-summary-writer': ('Executive Summary Writer', 'Write a publication-ready executive summary from a completed IC memo or research report.', 'deal-intelligence'),
    'finance-metrics-quickref': ('Finance Metrics Quick Reference', 'Look up SaaS finance metrics, formulas, and benchmarks instantly during analysis.', 'analysis'),
    'financial-model-builder': ('Financial Model Builder', 'Build a 3-tab operating model from source P&L or financial data. Requires data room access.', 'deal-intelligence'),
    'gtm-metrics-analyzer': ('GTM Metrics Analyzer', 'Calculate and package 48 GTM metrics across 6 families. Requires company metrics data.', 'deal-intelligence'),
    'ic-memo': ('IC Memo', 'Write a structured Investment Committee memo. 10-section structure with NTB registry and disaggregation table.', 'deal-intelligence'),
    'kpi-tree-builder': ('KPI Tree Builder', 'Build and audit company-specific KPI trees and management plan credibility assessments.', 'deal-intelligence'),
    'market-research': ('Market Research', 'Execute professional-grade market research: L4 market context, L3 customer insights, L2 competitive landscape.', 'research'),
    'mckinsey-consultant': ('McKinsey Consultant', 'McKinsey-level structured consulting: issue trees, hypothesis-driven analysis, Six Screening Questions.', 'analysis'),
    'ntb-diligence': ('NTB Diligence', '4-phase Need-to-Believe quality check with MOIC sum tolerance enforcement.', 'deal-intelligence'),
    'pattern-docx': ('Pattern DOCX', 'Generate on-brand Word documents using the Pattern template.', 'output'),
    'pattern-investment-pptx': ('Pattern Investment PPTX', 'Generate on-brand investment-grade PowerPoint decks in Pattern IC deck format.', 'output'),
    'pre-mortem': ('Pre-Mortem', '10-category failure taxonomy, compound failure paths, IC-facing risk narrative.', 'deal-intelligence'),
    'red-team': ('Red Team', 'Adversarial stress-test: attack vectors, kill scenarios, bear case, adversarial scorecard.', 'deal-intelligence'),
    'tam-sam-som-calculator': ('TAM/SAM/SOM Calculator', 'Size a market with top-down and bottom-up methodologies. Validates divergence, Year 1-3 projections.', 'research'),
    'writing-style': ('Writing Style', 'Governs prose quality, claim standards, and epistemic tagging [F/E/H].', 'output'),
    'Deck_Check': ('Deck Check', 'Review and audit presentation decks for structure, clarity, and completeness.', 'output'),
    'Deck_Refresh': ('Deck Refresh', 'Refresh and update existing presentation decks with new content.', 'output'),
    'executive-briefing': ('Executive Briefing', 'Transform research findings into executive-ready briefings for C-suite or board audiences.', 'output'),
    'managing-up': ('Managing Up', 'Framework for managing up effectively in a corporate environment.', 'communication'),
    'giving-presentations': ('Giving Presentations', 'Guidance on delivering effective presentations.', 'communication'),
    'statistics-fundamentals': ('Statistics Fundamentals', 'Core statistics concepts and their application in business analysis.', 'analysis'),
    'written-communication': ('Written Communication', 'Best practices for professional written communication.', 'communication'),
    'skill-authoring-workflow': ('Skill Authoring', 'Workflow for creating new skills following best practices.', 'meta'),
    'vibe-coding': ('Vibe Coding', 'Rapid prototyping and code generation workflow.', 'development'),
}

# Step 1: Add .claude-plugin/plugin.json to each skill folder in the repo
added = []
for folder, (name, desc, category) in skills.items():
    folder_path = os.path.join(repo_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    plugin_dir = os.path.join(folder_path, '.claude-plugin')
    os.makedirs(plugin_dir, exist_ok=True)
    plugin_json = {
        "name": folder.lower().replace('_', '-'),
        "version": "1.0.0",
        "description": desc,
        "category": category,
        "author": {"name": "Ian Lawrence"},
        "repository": "https://github.com/ian-lawrence423/Claude-skills"
    }
    with open(os.path.join(plugin_dir, 'plugin.json'), 'w') as f:
        json.dump(plugin_json, f, indent=2)
    added.append(folder)

print(f'Step 1: Added plugin.json to {len(added)} skill folders')

# Step 2: Create marketplace.json at repo root
marketplace_plugins = []
for folder, (name, desc, category) in skills.items():
    if not os.path.isdir(os.path.join(repo_dir, folder)):
        continue
    marketplace_plugins.append({
        "name": folder.lower().replace('_', '-'),
        "description": desc,
        "category": category,
        "source": "./" + folder,
        "author": {"name": "Ian Lawrence"}
    })

marketplace = {
    "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
    "name": "claude-skills",
    "description": "Ian Lawrence personal skill library for investment analysis, deal intelligence, and strategic research",
    "owner": {"name": "Ian Lawrence", "email": "ian.lawrence@pattern.com"},
    "plugins": sorted(marketplace_plugins, key=lambda x: x['name'])
}

mp_dir = os.path.join(repo_dir, '.claude-plugin')
os.makedirs(mp_dir, exist_ok=True)
with open(os.path.join(mp_dir, 'marketplace.json'), 'w') as f:
    json.dump(marketplace, f, indent=2)
print(f'Step 2: Created marketplace.json with {len(marketplace_plugins)} plugins')

# Step 3: Register in known_marketplaces.json
known_path = r'C:\Users\IanLawrence\.claude\plugins\known_marketplaces.json'
with open(known_path) as f:
    known = json.load(f)

known['claude-skills'] = {
    "source": {"source": "directory", "path": skills_dir},
    "installLocation": skills_dir,
    "lastUpdated": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')
}

with open(known_path, 'w') as f:
    json.dump(known, f, indent=2)
print('Step 3: Registered claude-skills marketplace in known_marketplaces.json')
print('Done — commit repo and restart Claude Code.')
