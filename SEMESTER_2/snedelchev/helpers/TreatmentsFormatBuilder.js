export class TreatmentsFormatBuilder {
    static formatCreateOrUpdate(data) {
        return {
            days_to_treatment_end: data.days_to_treatment_end ? +data.days_to_treatment_end : null,
            days_to_treatment_start: data.days_to_treatment_start ? +data.days_to_treatment_start : null,
            treatment_id: data.treatment_id,
            submitter_id: data.submitter_id,
            treatment_type: data.treatment_type,
            regimen_or_line_of_therapy: data.regimen_or_line_of_therapy,
            treatment_effect: data.treatment_effect,
            therapeutic_agents: data.therapeutic_agents,
            treatment_or_therapy: data.treatment_or_therapy,
            created_datetime: data.created_datetime,
            initial_disease_status: data.initial_disease_status,
            treatment_intent_type: data.treatment_intent_type,
            treatment_anatomic_site: data.treatment_anatomic_site,
            updated_datetime: data.updated_datetime,
            treatment_outcome: data.treatment_outcome,
            state: data.state
        };
    }
}
