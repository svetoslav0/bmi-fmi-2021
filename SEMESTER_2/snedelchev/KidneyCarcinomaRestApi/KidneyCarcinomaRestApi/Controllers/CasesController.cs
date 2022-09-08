namespace KidneyCarcinomaRestApi.Controllers
{
    using System.Collections.Generic;
    using Microsoft.AspNetCore.Mvc;

    using KidneyCarcinomaRestApi.Attributes;
    using KidneyCarcinomaRestApi.Interfaces;
    using KidneyCarcinomaRestApi.Models;
    using KidneyCarcinomaRestApi.Models.Parameters;

    [ApiController]
    [Route("[controller]")]
    [ExceptionHandler]
    public class CasesController : AbstractController
    {
        private readonly ICasesService casesService;

        public CasesController(ICasesService casesService)
        {
            this.casesService = casesService;
        }

        [HttpGet]
        [Route("")]
        [Paginated(DefaultLimit, DefaultOffset)]
        public IActionResult GetAll([FromQuery] AbstractParameters parameters)
        {
            List<Case> result = this.casesService.GetAllCases(parameters);
            long total = this.casesService.GetAllCasesCount();

            return this.BuildListResponse(result, total);
        }
    }
}