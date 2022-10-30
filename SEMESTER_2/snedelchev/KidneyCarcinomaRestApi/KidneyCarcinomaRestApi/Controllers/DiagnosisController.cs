namespace KidneyCarcinomaRestApi.Controllers
{
    using System;
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
        private readonly IDiagnosisService diagnosisService;

        public DiagnosisController(IDiagnosisService diagnosisService)
        {
            this.diagnosisService = diagnosisService;
        }

        [HttpGet]
        [Route("")]
        [Paginated(DefaultLimit, DefaultOffset)]
        public IActionResult GetAll([FromQuery] AbstractParameters parameters, [FromQuery] Diagnose searchParameters)
        {
            List<Diagnose> result = this.diagnosisService.GetAllDiagnoses(parameters, searchParameters);
            long total = this.diagnosisService.GetAllDiagnosesCount(searchParameters);

            return this.BuildListResponse(result, total);
        }

        [HttpGet]
        [Route("{id}")]
        public IActionResult GetById(string id)
        {
            Diagnose result = this.diagnosisService.GetDiagnoseById(id);
            return this.BuildResponse(result);
        }

        [HttpPost]
        [Route("")]
        public IActionResult Create([FromForm] Diagnose diagnose)
        {
            Diagnose saved = this.diagnosisService.Save(diagnose);
            return this.BuildResponse(saved);
        }

        [HttpPatch]
        [Route("{id}")]
        public IActionResult Update(string id, [FromForm] Diagnose diagnose)
        {
            Diagnose updated = this.diagnosisService.Update(id, diagnose);
            return this.BuildResponse(updated);
        }
    }
}
