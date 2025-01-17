# © 2018 Numigi
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Main Module",
    "version": "1.0.0",
    "author": "Numigi",
    "maintainer": "Numigi",
    "website": "https://www.numigi.com",
    "license": "LGPL-3",
    "category": "Other",
    "summary": "Install all addons required for testing.",
    "depends": [
        "stock_account",  # required for testing project_wip
        "purchase",  # required for testing project_wip_material
        "analytic_line_employee",
        "analytic_line_revenue",
        "project_analytic_group",
        "project_estimation",
        "project_estimation_material",
        "project_chatter",
        "project_cost_smart_button",
        "project_default_task_stage",
        "project_form_with_dates",
        "project_group_create",
        "project_hide_create_sale_order",
        "project_iteration",
        "project_iteration_parent_only",
        "project_iteration_parent_type_required",
        "project_iteration_sale_inheritance",
        "project_lump_sum",
        "project_material",
        "project_material_direct",
        "project_material_quantity_filters",
        "project_no_quick_create",
        "project_outsourcing",
        "project_portal_hide_timesheets",
        "project_portal_no_subtask",
        "project_portal_parent_task",
        "project_remaining_hours_update",
        "project_stage",
        "project_stage_allow_timesheet",
        "project_stage_no_quick_create",
        "project_task_analytic_lines",
        "project_task_analytic_lines_stock",
        "project_task_date_planned",
        "project_task_deadline_from_project",
        "project_task_editable_list_view",
        "project_task_full_text_search",
        "project_task_id_in_display_name",
        "project_task_link",
        "project_task_reference",
        "project_task_resource_type",
        "project_task_search_parent_subtask",
        "project_task_stage_external_mail",
        "project_task_subtask_same_project",
        "project_task_type",
        "project_template",
        "project_template_date_planned",
        "project_template_timesheet",
        "project_time_budget",
        "project_time_range",
        "project_timesheet_analytic_update",
        "project_type",
        "project_wip",
        "project_wip_material",
        "project_wip_outsourcing",
        "project_wip_supply_cost",
        "project_wip_timesheet",
        "timesheet_task_project_no_change",
    ],
    "installable": True,
}
