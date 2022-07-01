export class ExposureFormatBuilder {
    static formatCreate(data) {
        return {
            cigarettes_per_day: data.cigarettes_per_day ? +data.cigarettes_per_day : null,
            alcohol_history: data.alcohol_history,
            updated_datetime: data.updated_datetime,
            submitter_id: data.submitter_id,
            years_smoked: data.years_smoked ? +data.years_smoked : null,
            state: data.state,
            created_datetime: data.created_datetime,
            alcohol_intensity: data.alcohol_intensity
        };
    }
}
