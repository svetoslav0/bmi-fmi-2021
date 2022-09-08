namespace KidneyCarcinomaRestApi.Controllers
{
    using System.Collections.Generic;
    using Microsoft.AspNetCore.Mvc;

    using KidneyCarcinomaRestApi.Models;
    using KidneyCarcinomaRestApi.Attributes;
    using KidneyCarcinomaRestApi.Interfaces;
    using KidneyCarcinomaRestApi.Models.Parameters;

    [ApiController]
    [Route("[controller]")]
    [ExceptionHandler]
    public class DiagnosisController : AbstractController
    {
        private readonly IDiagnosesService diagnosesService;

        public DiagnosisController(IDiagnosesService diagnosesService)
        {
            this.diagnosesService = diagnosesService;
        }

        [HttpGet]
        [Route("")]
        [Paginated(DefaultLimit, DefaultOffset)]
        public IActionResult GetAll([FromQuery] AbstractParameters parameters, [FromQuery] Diagnose searchParameters)
        {
            List<Diagnose> result = this.diagnosesService.GetAllDiagnoses(parameters, searchParameters);
            long total = this.diagnosesService.GetAllDiagnosesCount(searchParameters);

            return this.BuildListResponse(result, total);
        }

        [HttpGet]
        [Route("{id}")]
        public IActionResult GetById(string id)
        {
            var result = this.diagnosesService.GetDiagnoseById(id);

            return this.BuildResponse(result);
        }
    }
}
