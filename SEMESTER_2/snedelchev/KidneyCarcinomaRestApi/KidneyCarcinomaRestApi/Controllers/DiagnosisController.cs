namespace KidneyCarcinomaRestApi.Controllers
{
    using System.Collections.Generic;
    using Microsoft.AspNetCore.Mvc;

    using KidneyCarcinomaRestApi.Models;
    using KidneyCarcinomaRestApi.Services;
    using KidneyCarcinomaRestApi.Attributes;
    using KidneyCarcinomaRestApi.Models.Parameters;

    [ApiController]
    [Route("[controller]")]
    [ExceptionHandler]
    public class DiagnosisController : AbstractController
    {
        private readonly MongoDbService mongoDbService;

        public DiagnosisController(MongoDbService mongoDbService)
        {
            this.mongoDbService = mongoDbService;
        }

        [HttpGet]
        [Route("")]
        [Paginated(DefaultLimit, DefaultOffset)]
        public IActionResult GetAll([FromQuery] AbstractParameters parameters)
        {
            List<Diagnose> result = this.mongoDbService.GetAllDiagnoses(parameters).Result;
            long total = this.mongoDbService.GetAllDiagnosesCount();

            return this.BuildListResponse(result, total);
        }

        [HttpGet]
        [Route("{id}")]
        public IActionResult GetById(string id)
        {
            var result = this.mongoDbService.GetDiagnoseById(id);

            return this.BuildResponse(result);
        }
    }
}
