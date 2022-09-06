namespace KidneyCarcinomaRestApi.Controllers
{
    using Microsoft.AspNetCore.Mvc;

    using KidneyCarcinomaRestApi.Models.Responses;
    using Newtonsoft.Json;

    public abstract class AbstractController : Controller
    {
        protected const int DefaultLimit = 100;
        protected const int DefaultOffset = 0;

        private readonly string DefaultContentType = "application/json";

        protected IActionResult BuildListResponse(object content, long total = 0)
        {
            DataListResponse response = new DataListResponse
            {
                Data = content,
                Total = total
            };

            return this.GetContentResult(response);
        }

        protected IActionResult BuildResponse(object content)
        {
            DataResponse response = new DataResponse
            {
                Data = content
            };

            return this.GetContentResult(response);
        }

        private ContentResult GetContentResult(DataResponse response)
        {
            return this.Content(JsonConvert.SerializeObject(response), DefaultContentType);
        }
    }
}
