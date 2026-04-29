from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from pathlib import Path

OUT = Path(__file__).parent / 'gtm_metrics_template.xlsx'
OUT.parent.mkdir(parents=True, exist_ok=True)

header_fill = PatternFill('solid', fgColor='1F4E78')
section_fill = PatternFill('solid', fgColor='D9EAF7')
light_fill = PatternFill('solid', fgColor='F5F9FC')
white_font = Font(color='FFFFFF', bold=True)
bold = Font(bold=True)
thin = Side(style='thin', color='D0D7DE')
border = Border(left=thin, right=thin, top=thin, bottom=thin)
center = Alignment(vertical='center')
wrap = Alignment(wrap_text=True, vertical='top')

input_rows = [
    ('Company & Reporting Context','business_model','Business Model','e.g., B2B SaaS, usage-based SaaS, hybrid, PLG, SLG','Required',None),
    ('Company & Reporting Context','primary_revenue_metric','Primary Revenue Metric','ARR, MRR, CARR, bookings, billings, GAAP revenue','Required',None),
    ('Company & Reporting Context','reporting_cadence','Reporting Cadence','Monthly, quarterly, annual, or LTM','Required',None),
    ('Company & Reporting Context','analysis_period','Analysis Period','Period being analyzed','Required',None),
    ('Company & Reporting Context','segment_scheme','Segmentation Scheme','SMB, MM, Enterprise, geo, product, channel, etc.','Optional',None),
    ('Revenue & ARR','beginning_arr','Beginning ARR','ARR at start of period','Required for ARR funnel',0),
    ('Revenue & ARR','new_logo_arr','New Logo ARR','ARR from new customers in period','Required for ARR funnel',0),
    ('Revenue & ARR','expansion_arr','Expansion ARR','ARR expansion from existing customers','Required for ARR funnel/retention',0),
    ('Revenue & ARR','upsell_arr','Upsell ARR','Expansion from same product / contract uplift','Optional',0),
    ('Revenue & ARR','cross_sell_arr','Cross-sell ARR','Expansion from new product / contract','Optional',0),
    ('Revenue & ARR','downsell_arr','Downsell ARR','ARR lost from customer downgrades','Required for ARR funnel/retention',0),
    ('Revenue & ARR','logo_churn_arr','Logo Churn ARR','ARR lost from customer churn','Required for ARR funnel/retention',0),
    ('Revenue & ARR','ending_arr','Ending ARR','ARR at end of period if already known','Optional / validation',0),
    ('Revenue & ARR','bookings','Bookings','Total contract value signed in period','Optional',0),
    ('Revenue & ARR','billings','Billings','Amount invoiced in period','Optional',0),
    ('Revenue & ARR','revenue','Revenue','Recognized revenue in period','Optional',0),
    ('Revenue & ARR','deferred_revenue','Deferred Revenue','Billings less recognized revenue','Optional',0),
    ('Customer & Retention','bop_customers','Beginning Customer Count','Customers at start of period','Required for logo retention',0),
    ('Customer & Retention','eop_customers','Ending Customer Count','Customers at end of period','Required for logo retention',0),
    ('Customer & Retention','gross_new_logo_customers','Gross New Logo Customers','New logos acquired in period','Required for CAC',0),
    ('Customer & Retention','churned_customers','Churned Customers','Customers lost in period','Required for logo churn',0),
    ('Customer & Retention','logo_churn_rate','Logo Churn Rate','If already calculated, can be provided directly','Optional / shortcut',0),
    ('Customer & Retention','avg_arr_per_customer','Average ARR per Customer','Average ARR per retained customer','Required for LTV',0),
    ('Customer & Retention','dau','Daily Active Users','Customer-level or aggregate DAU','Optional',0),
    ('Customer & Retention','mau','Monthly Active Users','Customer-level or aggregate MAU','Optional',0),
    ('Customer & Retention','total_users','Total Users','Total licensed / relevant users','Optional',0),
    ('Customer & Retention','feature_active_users','Feature Active Users','Users actively using a feature','Optional',0),
    ('Customer & Retention','expected_implementation_days','Expected Implementation Days','Promised or target implementation duration','Optional',0),
    ('Customer & Retention','actual_implementation_days','Actual Implementation Days','Observed implementation duration','Optional',0),
    ('Customer & Retention','promoter_pct','Promoter %','Percent of promoters for NPS','Optional',0),
    ('Customer & Retention','detractor_pct','Detractor %','Percent of detractors for NPS','Optional',0),
    ('Customer & Retention','satisfied_responses','Satisfied Responses','Positive CSAT responses','Optional',0),
    ('Customer & Retention','total_responses','Total Responses','Total survey responses','Optional',0),
    ('Funnel & Pipeline','pipeline_dollars','Pipeline $','Unweighted pipeline value for period','Required for pipeline coverage',0),
    ('Funnel & Pipeline','weighted_pipeline_dollars','Weighted Pipeline $','Forecast-weighted pipeline value','Optional / preferred',0),
    ('Funnel & Pipeline','sales_target','Sales Target','Bookings / ARR target for period','Required for coverage',0),
    ('Funnel & Pipeline','forecast_dollars','Forecast $','Forecast for period','Required for forecast vs target',0),
    ('Funnel & Pipeline','closed_won_opportunities','Closed Won Opportunities','Count of won opportunities','Optional',0),
    ('Funnel & Pipeline','closed_lost_opportunities','Closed Lost Opportunities','Count of lost opportunities','Optional',0),
    ('Funnel & Pipeline','opportunities_created','Opportunities Created in Period','Used for close rate','Optional',0),
    ('Funnel & Pipeline','closed_won_same_period','Closed Won in Same Period','Used for close rate','Optional',0),
    ('Funnel & Pipeline','sql_count','SQL Count','Total sales qualified leads','Optional',0),
    ('Funnel & Pipeline','closed_won_sql','Closed Won SQLs','SQLs that closed won','Optional',0),
    ('Funnel & Pipeline','stage_forecast_probability','Average Stage Forecast Probability','If using a simplified weighted forecast','Optional',0),
    ('Efficiency & Economics','sm_opex','S&M OpEx (Current Period)','Sales & marketing operating expense in current period','Required for several metrics',0),
    ('Efficiency & Economics','prior_qtr_sm_opex','Prior Quarter S&M OpEx','Preferred for magic number and time-adjusted CAC','Required for lagged metrics',0),
    ('Efficiency & Economics','gross_profit','Gross Profit','Total gross profit in period','Required for gross margin',0),
    ('Efficiency & Economics','total_revenue','Total Revenue','Total revenue in period','Required for gross margin',0),
    ('Efficiency & Economics','subscription_gross_profit','Subscription Gross Profit','Gross profit from subscription revenue line','Optional',0),
    ('Efficiency & Economics','subscription_revenue','Subscription Revenue','Revenue from subscription line only','Optional',0),
    ('Efficiency & Economics','services_gross_profit','Services Gross Profit','Gross profit from professional services','Optional',0),
    ('Efficiency & Economics','services_revenue','Services Revenue','Revenue from professional services','Optional',0),
    ('Efficiency & Economics','gross_margin_pct','Gross Margin %','Can be input directly if already calculated','Optional / shortcut',0),
    ('Efficiency & Economics','channel_spend','Channel Spend','Spend for a specific channel','Optional',0),
    ('Efficiency & Economics','channel_new_logos','Channel New Logos','Customers acquired via channel','Optional',0),
    ('Team & Productivity','avg_sm_ftes','Average S&M FTEs','Average S&M employees in period','Required for FTE metrics',0),
    ('Team & Productivity','qcr_count','Quota-Carrying Reps','Average QCRs in period','Required for rep productivity/capacity',0),
    ('Team & Productivity','csm_count','CSM Count','Customer success managers','Optional',0),
    ('Team & Productivity','sales_manager_count','Sales Manager Count','AE managers','Optional',0),
    ('Team & Productivity','sdr_count','SDR / BDR Count','Sales development / business development reps','Optional',0),
    ('Team & Productivity','qcr_departed','QCRs Departed','Quota-carrying reps departed in period','Optional',0),
    ('Team & Productivity','quota_allocated','Quota Allocated','Total allocated quota in period','Required for attainment',0),
    ('Team & Productivity','quota_attained','Quota Attained','Total quota achieved in period','Required for attainment',0),
    ('Team & Productivity','qcrs_attaining_100','QCRs Attaining 100%+','Count of reps hitting quota','Optional',0),
    ('Team & Productivity','qcr_retention_rate','QCR Retention Rate','Percent of QCRs retained in period','Required for capacity if used',0),
    ('Team & Productivity','reps_first_full_ramp_period','Reps in First Fully Ramped Period','Denominator for ramp rate','Optional',0),
    ('Team & Productivity','reps_hit_quota_first_full_ramp','Reps Hitting Quota in First Fully Ramped Period','Numerator for ramp rate','Optional',0),
    ('Planning / Forecast','plan_net_new_bookings','Plan Net New Bookings','Budgeted net new bookings','Optional',0),
    ('Planning / Forecast','plan_gross_new_bookings','Plan Gross New Bookings','Budgeted gross new bookings','Optional',0),
    ('Planning / Forecast','plan_ending_arr','Plan Ending ARR','Budgeted ending ARR','Optional',0),
    ('Planning / Forecast','actual_yoy_arr_growth_pct','Actual YoY ARR Growth %','If actual growth already calculated','Optional',0),
    ('Planning / Forecast','plan_yoy_arr_growth_pct','Plan YoY ARR Growth %','Budgeted YoY ARR growth','Optional',0),
    ('Planning / Forecast','actual_fcf','Actual Free Cash Flow','Optional',0),
    ('Planning / Forecast','plan_fcf','Plan Free Cash Flow','Optional',0),
    ('Planning / Forecast','revenue_guidance','Revenue Guidance','Management guidance','Optional',0),
    ('Planning / Forecast','consensus_estimate','Consensus Estimate','Public-company context only','Optional',0),
]

metrics = [
    ('Growth Drivers','gross_new_arr','Gross New ARR','Derived','New Logo ARR + Expansion ARR','new_logo_arr, expansion_arr', '=IF(COUNTIF(Input_Fields!$B:$B,"new_logo_arr")*COUNTIF(Input_Fields!$B:$B,"expansion_arr")=0,"",XLOOKUP("new_logo_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")+XLOOKUP("expansion_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,""))'),
    ('Growth Drivers','churned_arr','Churned ARR','Derived','Downsell ARR + Logo Churn ARR','downsell_arr, logo_churn_arr', '=IF(COUNTIF(Input_Fields!$B:$B,"downsell_arr")*COUNTIF(Input_Fields!$B:$B,"logo_churn_arr")=0,"",XLOOKUP("downsell_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")+XLOOKUP("logo_churn_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,""))'),
    ('Growth Drivers','net_new_arr','Net New ARR','Derived','Gross New ARR - Churned ARR','new_logo_arr, expansion_arr, downsell_arr, logo_churn_arr', '=IFERROR(G2-G3,"")'),
    ('Growth Drivers','ending_arr_calc','Ending ARR (Calculated)','Derived','Beginning ARR + Net New ARR','beginning_arr, new_logo_arr, expansion_arr, downsell_arr, logo_churn_arr', '=IFERROR(XLOOKUP("beginning_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")+G4,"")'),
    ('Growth Drivers','arr_growth_yoy','ARR Growth YoY %','Derived','((EOP ARR / EOP ARR 12 months ago) - 1) * 100','Requires prior-year EOP ARR upload', ''),
    ('Growth Drivers','new_logo_mix','% Gross New ARR from New Logo','Derived','New Logo ARR / Gross New ARR','new_logo_arr, expansion_arr', '=IFERROR(XLOOKUP("new_logo_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/G2,"")'),
    ('Growth Drivers','expansion_mix','% Gross New ARR from Expansion','Derived','Expansion ARR / Gross New ARR','new_logo_arr, expansion_arr', '=IFERROR(XLOOKUP("expansion_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/G2,"")'),
    ('Sales Funnel','pipeline_coverage','Pipeline Coverage','Derived','Pipeline $ / Sales Target','pipeline_dollars, sales_target', '=IFERROR(XLOOKUP("pipeline_dollars",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("sales_target",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Sales Funnel','weighted_pipeline_coverage','Weighted Pipeline Coverage','Derived','Weighted Pipeline $ / Sales Target','weighted_pipeline_dollars, sales_target', '=IFERROR(XLOOKUP("weighted_pipeline_dollars",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("sales_target",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Sales Funnel','win_rate','Win Rate','Derived','Closed Won / (Closed Won + Closed Lost)','closed_won_opportunities, closed_lost_opportunities', '=IFERROR(XLOOKUP("closed_won_opportunities",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/(XLOOKUP("closed_won_opportunities",Input_Fields!$B:$B,Input_Fields!$F:$F,"")+XLOOKUP("closed_lost_opportunities",Input_Fields!$B:$B,Input_Fields!$F:$F,"")),"")'),
    ('Sales Funnel','close_rate','Close Rate','Derived','Closed Won in same period / Opportunities created in period','closed_won_same_period, opportunities_created', '=IFERROR(XLOOKUP("closed_won_same_period",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("opportunities_created",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Sales Funnel','sql_to_closed_won','SQL to Closed Won','Derived','Closed Won SQLs / SQL Count','closed_won_sql, sql_count', '=IFERROR(XLOOKUP("closed_won_sql",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("sql_count",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Sales Funnel','forecast_pct_target','Forecast as % of Sales Target','Derived','Forecast $ / Sales Target','forecast_dollars, sales_target', '=IFERROR(XLOOKUP("forecast_dollars",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("sales_target",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Retention','quarterly_ndr','Quarterly Annualized NDR','Derived','1 + ((Quarter Expansion ARR - Quarter Churned ARR) * 4) / avg(BOQ ARR + EOQ ARR)','beginning_arr, ending_arr or calculated ending arr, expansion_arr, downsell_arr, logo_churn_arr', '=IFERROR(1+(((XLOOKUP("expansion_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")-(XLOOKUP("downsell_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")+XLOOKUP("logo_churn_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")))*4)/AVERAGE(XLOOKUP("beginning_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,""),IF(XLOOKUP("ending_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")="",G5,XLOOKUP("ending_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")))),"")'),
    ('Retention','quarterly_gdr','Quarterly Annualized GDR','Derived','1 - (Quarter Gross Churned ARR * 4) / avg(BOQ ARR + EOQ ARR)','beginning_arr, ending_arr or calculated ending arr, downsell_arr, logo_churn_arr', '=IFERROR(1-((((XLOOKUP("downsell_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")+XLOOKUP("logo_churn_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,""))*4)/AVERAGE(XLOOKUP("beginning_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,""),IF(XLOOKUP("ending_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")="",G5,XLOOKUP("ending_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")))),"")'),
    ('Retention','logo_retention','Logo Retention','Derived','1 - Churned Customers / avg(BOP Customers + EOP Customers)','bop_customers, eop_customers, churned_customers', '=IFERROR(1-(XLOOKUP("churned_customers",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/AVERAGE(XLOOKUP("bop_customers",Input_Fields!$B:$B,Input_Fields!$F:$F,""),XLOOKUP("eop_customers",Input_Fields!$B:$B,Input_Fields!$F:$F,""))),"")'),
    ('Retention','logo_churn','Logo Churn','Derived','Churned Customers / avg(BOP Customers + EOP Customers)','bop_customers, eop_customers, churned_customers', '=IFERROR(XLOOKUP("churned_customers",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/AVERAGE(XLOOKUP("bop_customers",Input_Fields!$B:$B,Input_Fields!$F:$F,""),XLOOKUP("eop_customers",Input_Fields!$B:$B,Input_Fields!$F:$F,"")),"")'),
    ('Retention','dau_rate','DAU Rate','Derived','DAU / Total Users','dau, total_users', '=IFERROR(XLOOKUP("dau",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("total_users",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Retention','mau_rate','MAU Rate','Derived','MAU / Total Users','mau, total_users', '=IFERROR(XLOOKUP("mau",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("total_users",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Retention','adoption_rate','Adoption Rate','Derived','Feature Active Users / Total Users','feature_active_users, total_users', '=IFERROR(XLOOKUP("feature_active_users",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("total_users",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Retention','stickiness_rate','Stickiness Rate','Derived','DAU / MAU','dau, mau', '=IFERROR(XLOOKUP("dau",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("mau",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Retention','time_to_implement_vs_goal','Time to Implement vs Goal','Derived','Actual Implementation Days / Expected Implementation Days','actual_implementation_days, expected_implementation_days', '=IFERROR(XLOOKUP("actual_implementation_days",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("expected_implementation_days",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Retention','nps','NPS','Derived','Promoter % - Detractor %','promoter_pct, detractor_pct', '=IFERROR(XLOOKUP("promoter_pct",Input_Fields!$B:$B,Input_Fields!$F:$F,"")-XLOOKUP("detractor_pct",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Retention','csat','CSAT','Derived','Satisfied Responses / Total Responses','satisfied_responses, total_responses', '=IFERROR(XLOOKUP("satisfied_responses",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("total_responses",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Efficiency & Economics','gross_margin','Gross Margin','Derived','Gross Profit / Total Revenue','gross_profit, total_revenue', '=IFERROR(XLOOKUP("gross_profit",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("total_revenue",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Efficiency & Economics','subscription_gm','Subscription Gross Margin','Derived','Subscription Gross Profit / Subscription Revenue','subscription_gross_profit, subscription_revenue', '=IFERROR(XLOOKUP("subscription_gross_profit",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("subscription_revenue",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Efficiency & Economics','services_gm','Services Gross Margin','Derived','Services Gross Profit / Services Revenue','services_gross_profit, services_revenue', '=IFERROR(XLOOKUP("services_gross_profit",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("services_revenue",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Efficiency & Economics','net_magic_number','Net Magic Number','Derived','Current Quarter Net New ARR / Prior Quarter S&M OpEx','new_logo_arr, expansion_arr, downsell_arr, logo_churn_arr, prior_qtr_sm_opex', '=IFERROR(G4/XLOOKUP("prior_qtr_sm_opex",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Efficiency & Economics','gross_magic_number','Gross Magic Number','Derived','Current Quarter Gross New ARR / Prior Quarter S&M OpEx','new_logo_arr, expansion_arr, prior_qtr_sm_opex', '=IFERROR(G2/XLOOKUP("prior_qtr_sm_opex",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Efficiency & Economics','simple_cac','Simple CAC','Derived','S&M OpEx / Gross New Logo Customers','sm_opex, gross_new_logo_customers', '=IFERROR(XLOOKUP("sm_opex",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("gross_new_logo_customers",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Efficiency & Economics','time_adjusted_cac','Time-Adjusted CAC','Derived','Prior Quarter S&M OpEx / Gross New Logo Customers This Quarter','prior_qtr_sm_opex, gross_new_logo_customers', '=IFERROR(XLOOKUP("prior_qtr_sm_opex",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("gross_new_logo_customers",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Efficiency & Economics','simple_ltv','Simple LTV','Derived','(ARR per Customer * Gross Margin) / Logo Churn Rate','avg_arr_per_customer, gross_margin or gross_margin_pct, logo_churn or provided logo_churn_rate', '=IFERROR((XLOOKUP("avg_arr_per_customer",Input_Fields!$B:$B,Input_Fields!$F:$F,"")*IF(XLOOKUP("gross_margin_pct",Input_Fields!$B:$B,Input_Fields!$F:$F,"")="",G26,XLOOKUP("gross_margin_pct",Input_Fields!$B:$B,Input_Fields!$F:$F,"")))/IF(XLOOKUP("logo_churn_rate",Input_Fields!$B:$B,Input_Fields!$F:$F,"")="",G18,XLOOKUP("logo_churn_rate",Input_Fields!$B:$B,Input_Fields!$F:$F,"")),"")'),
    ('Efficiency & Economics','ltv_cac','LTV / CAC','Derived','Customer LTV / Customer Acquisition Cost','avg_arr_per_customer, margin, churn, sm_opex, gross_new_logo_customers', '=IFERROR(G33/G31,"")'),
    ('Efficiency & Economics','payback_period','Payback Period','Derived','CAC / (ARR per Customer * Gross Margin)','avg_arr_per_customer, margin, sm_opex, gross_new_logo_customers', '=IFERROR(G31/(XLOOKUP("avg_arr_per_customer",Input_Fields!$B:$B,Input_Fields!$F:$F,"")*IF(XLOOKUP("gross_margin_pct",Input_Fields!$B:$B,Input_Fields!$F:$F,"")="",G26,XLOOKUP("gross_margin_pct",Input_Fields!$B:$B,Input_Fields!$F:$F,""))),"")'),
    ('Team & Productivity','sm_opex_per_fte','S&M OpEx per S&M FTE','Derived','(Quarter S&M OpEx * 4) / Average S&M FTEs','sm_opex, avg_sm_ftes', '=IFERROR((XLOOKUP("sm_opex",Input_Fields!$B:$B,Input_Fields!$F:$F,"")*4)/XLOOKUP("avg_sm_ftes",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','ae_per_csm','AE per CSM','Derived','Quota-Carrying AEs / CSMs','qcr_count, csm_count', '=IFERROR(XLOOKUP("qcr_count",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("csm_count",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','ae_per_manager','AE per Sales Manager','Derived','Quota-Carrying AEs / Sales Managers','qcr_count, sales_manager_count', '=IFERROR(XLOOKUP("qcr_count",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("sales_manager_count",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','ae_per_sdr','AE per SDR','Derived','Quota-Carrying AEs / SDRs','qcr_count, sdr_count', '=IFERROR(XLOOKUP("qcr_count",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("sdr_count",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','employee_attrition','Employee Attrition','Derived','QCRs Departed / Average QCRs in Period','qcr_departed, qcr_count', '=IFERROR(XLOOKUP("qcr_departed",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("qcr_count",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','nnarr_per_sm_fte','NNARR per S&M FTE','Derived','(Net New ARR * 4) / Average S&M FTEs','new_logo_arr, expansion_arr, downsell_arr, logo_churn_arr, avg_sm_ftes', '=IFERROR((G4*4)/XLOOKUP("avg_sm_ftes",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','sales_capacity','Sales Capacity','Derived','Allocated Quota * Quota Attainment % * QCR Retention Rate','quota_allocated, quota_attained, qcr_retention_rate', '=IFERROR(XLOOKUP("quota_allocated",Input_Fields!$B:$B,Input_Fields!$F:$F,"")*(XLOOKUP("quota_attained",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("quota_allocated",Input_Fields!$B:$B,Input_Fields!$F:$F,""))*XLOOKUP("qcr_retention_rate",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','capacity_per_qcr','Capacity per QCR','Derived','Sales Capacity / QCR Count','quota_allocated, quota_attained, qcr_retention_rate, qcr_count', '=IFERROR(G42/XLOOKUP("qcr_count",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','net_productivity','Net Productivity','Derived','Net New ARR / Average QCRs','new_logo_arr, expansion_arr, downsell_arr, logo_churn_arr, qcr_count', '=IFERROR(G4/XLOOKUP("qcr_count",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','team_quota_attainment','Team Quota Attainment','Derived','QCRs attaining 100%+ / total QCRs','qcrs_attaining_100, qcr_count', '=IFERROR(XLOOKUP("qcrs_attaining_100",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("qcr_count",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','rep_attainment','Rep Attainment','Derived','Quota Attained / Quota Allocated','quota_attained, quota_allocated', '=IFERROR(XLOOKUP("quota_attained",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("quota_allocated",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Team & Productivity','ramp_rate','Ramp Rate','Derived','Reps hitting quota in first fully ramped period / reps in first fully ramped period','reps_hit_quota_first_full_ramp, reps_first_full_ramp_period', '=IFERROR(XLOOKUP("reps_hit_quota_first_full_ramp",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("reps_first_full_ramp_period",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Fiscal Maturity','net_new_bookings_attainment','Net New Bookings Attainment','Derived','Actual Net New Bookings / Plan Net New Bookings','net new ARR approximation or actual net bookings, plan_net_new_bookings', '=IFERROR(G4/XLOOKUP("plan_net_new_bookings",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Fiscal Maturity','gross_new_bookings_attainment','Gross New Bookings Attainment','Derived','Actual Gross New Bookings / Plan Gross New Bookings','gross_new_arr, plan_gross_new_bookings', '=IFERROR(G2/XLOOKUP("plan_gross_new_bookings",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Fiscal Maturity','ending_arr_attainment','Ending ARR Attainment','Derived','Actual Ending ARR / Plan Ending ARR','ending arr or calculated ending arr, plan_ending_arr', '=IFERROR(IF(XLOOKUP("ending_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,"")="",G5,XLOOKUP("ending_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,""))/XLOOKUP("plan_ending_arr",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Fiscal Maturity','yoy_arr_growth_attainment','YoY ARR Growth Attainment','Derived','Actual YoY ARR Growth / Plan YoY ARR Growth','actual_yoy_arr_growth_pct, plan_yoy_arr_growth_pct', '=IFERROR(XLOOKUP("actual_yoy_arr_growth_pct",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("plan_yoy_arr_growth_pct",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Fiscal Maturity','fcf_attainment','Free Cash Flow Attainment','Derived','Actual FCF / Plan FCF','actual_fcf, plan_fcf', '=IFERROR(XLOOKUP("actual_fcf",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("plan_fcf",Input_Fields!$B:$B,Input_Fields!$F:$F,""),"")'),
    ('Fiscal Maturity','beat_vs_guidance','Beat Against Revenue Guidance','Derived','(Actual Revenue / Revenue Guidance) - 1','revenue, revenue_guidance', '=IFERROR((XLOOKUP("revenue",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("revenue_guidance",Input_Fields!$B:$B,Input_Fields!$F:$F,""))-1,"")'),
    ('Fiscal Maturity','beat_vs_consensus','Beat Against Revenue Consensus','Derived','(Actual Revenue / Consensus Estimate) - 1','revenue, consensus_estimate', '=IFERROR((XLOOKUP("revenue",Input_Fields!$B:$B,Input_Fields!$F:$F,"")/XLOOKUP("consensus_estimate",Input_Fields!$B:$B,Input_Fields!$F:$F,""))-1,"")'),
]

wb = Workbook()
ws = wb.active
ws.title = 'README'
ws['A1'] = 'GTM Metrics Analyzer Template'
ws['A1'].font = Font(size=14, bold=True)
ws['A3'] = 'Purpose'
ws['A3'].font = bold
ws['A4'] = 'Use this workbook to separate required uploaded inputs from derived GTM calculations and then surface a clean diagnostic output in one place.'
ws['A6'] = 'Tab order'
ws['A6'].font = bold
for i, line in enumerate([
    '1. Input_Fields: populate only user-provided fields from uploaded source files.',
    '2. Metric_Calcs: review formulas, required inputs, and calculated values.',
    '3. Diagnostic_Output: clean summary of the most decision-useful GTM metrics.',
    'Do not overwrite raw source exports. Add them as separate tabs if needed.'
], start=7):
    ws[f'A{i}'] = line
ws.column_dimensions['A'].width = 110
for row in range(1, 12):
    ws.row_dimensions[row].height = 22

inp = wb.create_sheet('Input_Fields')
headers = ['Section','Input Key','Input Label','Definition / What to Upload','Input Requirement','User Value','Notes']
inp.append(headers)
for c in range(1, len(headers)+1):
    cell = inp.cell(1,c)
    cell.fill = header_fill; cell.font = white_font; cell.border = border; cell.alignment = center
for row in input_rows:
    inp.append(list(row[:-1]) + [row[-1]])
for r in range(2, inp.max_row+1):
    for c in range(1, inp.max_column+1):
        cell = inp.cell(r,c)
        cell.border = border
        cell.alignment = wrap
        if c == 1 and r > 2 and inp.cell(r,1).value != inp.cell(r-1,1).value:
            for cc in range(1, inp.max_column+1):
                inp.cell(r,cc).fill = section_fill
for col, width in {'A':24,'B':28,'C':28,'D':42,'E':22,'F':16,'G':22}.items():
    inp.column_dimensions[col].width = width
input_tab = Table(displayName='InputFields', ref=f'A1:G{inp.max_row}')
input_tab.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
inp.add_table(input_tab)
inp.freeze_panes = 'A2'

calc = wb.create_sheet('Metric_Calcs')
calc_headers = ['Metric Family','Metric Key','Metric Name','Type','Formula / Logic','Required Inputs','Calculated Value','Comments']
calc.append(calc_headers)
for c in range(1, len(calc_headers)+1):
    cell = calc.cell(1,c)
    cell.fill = header_fill; cell.font = white_font; cell.border = border; cell.alignment = center
for row in metrics:
    calc.append(list(row) + [''])
for r in range(2, calc.max_row+1):
    for c in range(1, calc.max_column+1):
        cell = calc.cell(r,c)
        cell.border = border
        cell.alignment = wrap
        if c == 1 and r > 2 and calc.cell(r,1).value != calc.cell(r-1,1).value:
            for cc in range(1, calc.max_column+1):
                calc.cell(r,cc).fill = section_fill
for col, width in {'A':20,'B':22,'C':28,'D':10,'E':34,'F':34,'G':16,'H':22}.items():
    calc.column_dimensions[col].width = width
for r in range(2, calc.max_row+1):
    calc.cell(r,7).number_format = '0.0%;-0.0%;0.0%' if any(k in calc.cell(r,2).value for k in ['rate','retention','attainment','margin','coverage','pct','guidance','consensus']) else '#,##0.00'
metric_tab = Table(displayName='MetricCalcs', ref=f'A1:H{calc.max_row}')
metric_tab.tableStyleInfo = TableStyleInfo(name='TableStyleMedium9', showRowStripes=True)
calc.add_table(metric_tab)
calc.freeze_panes = 'A2'

out = wb.create_sheet('Diagnostic_Output')
out['A1'] = 'Diagnostic Output'
out['A1'].font = Font(size=14, bold=True)
out['A3'] = 'Populate Input_Fields from uploaded source files. This tab pulls selected derived metrics automatically.'
out['A5'] = 'Metric'
out['B5'] = 'Value'
out['C5'] = 'Notes'
for c in range(1,4):
    out.cell(5,c).fill = header_fill; out.cell(5,c).font = white_font; out.cell(5,c).border = border
summary_metrics = [
    ('Gross New ARR','gross_new_arr','ARR funnel'),
    ('Net New ARR','net_new_arr','ARR funnel'),
    ('Ending ARR (Calculated)','ending_arr_calc','ARR funnel'),
    ('Pipeline Coverage','pipeline_coverage','Sales funnel'),
    ('Weighted Pipeline Coverage','weighted_pipeline_coverage','Sales funnel'),
    ('Win Rate','win_rate','Sales funnel'),
    ('Quarterly Annualized NDR','quarterly_ndr','Retention'),
    ('Quarterly Annualized GDR','quarterly_gdr','Retention'),
    ('Logo Retention','logo_retention','Retention'),
    ('Gross Margin','gross_margin','Economics'),
    ('Net Magic Number','net_magic_number','Economics'),
    ('Simple CAC','simple_cac','Economics'),
    ('Simple LTV','simple_ltv','Economics'),
    ('LTV / CAC','ltv_cac','Economics'),
    ('S&M OpEx per FTE','sm_opex_per_fte','Productivity'),
    ('NNARR per S&M FTE','nnarr_per_sm_fte','Productivity'),
    ('Sales Capacity','sales_capacity','Productivity'),
    ('Rep Attainment','rep_attainment','Productivity'),
    ('Ramp Rate','ramp_rate','Productivity'),
    ('Ending ARR Attainment','ending_arr_attainment','Fiscal maturity'),
]
start = 6
for i,(label,key,note) in enumerate(summary_metrics, start=start):
    out[f'A{i}'] = label
    out[f'B{i}'] = f'=XLOOKUP("{key}",Metric_Calcs!$B:$B,Metric_Calcs!$G:$G,"")'
    out[f'C{i}'] = note
    for c in range(1,4):
        out.cell(i,c).border = border
        out.cell(i,c).alignment = wrap
out['E5'] = 'Missing Required Inputs'
out['E5'].fill = header_fill; out['E5'].font = white_font; out['E5'].border = border
out['E6'] = '=TEXTJOIN(CHAR(10),TRUE,FILTER(Input_Fields!$C$2:$C$999,(Input_Fields!$E$2:$E$999<>"Optional")*(Input_Fields!$F$2:$F$999=""),""))'
out['E6'].alignment = wrap
out['E6'].border = border
out.column_dimensions['A'].width = 30
out.column_dimensions['B'].width = 16
out.column_dimensions['C'].width = 22
out.column_dimensions['E'].width = 38
for r in range(6, start+len(summary_metrics)):
    if any(k in out[f'A{r}'].value.lower() for k in ['rate','retention','margin','attainment','coverage']):
        out[f'B{r}'].number_format = '0.0%'
    elif any(k in out[f'A{r}'].value.lower() for k in ['cac','ltv','arr','opex','capacity']):
        out[f'B{r}'].number_format = '$#,##0.00'

for sheet in [ws, inp, calc, out]:
    for row in sheet.iter_rows():
        for cell in row:
            if cell.row > 1:
                cell.border = border

wb.save(OUT)
print(f'Wrote {OUT}')
