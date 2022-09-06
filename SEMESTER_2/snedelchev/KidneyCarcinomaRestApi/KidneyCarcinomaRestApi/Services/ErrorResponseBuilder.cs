namespace KidneyCarcinomaRestApi.Services
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Net;
    using System.Reflection;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Filters;
    using Microsoft.AspNetCore.Mvc.ModelBinding;
    
    using KidneyCarcinomaRestApi.Exceptions;
    using KidneyCarcinomaRestApi.Helpers;
    using KidneyCarcinomaRestApi.Models.Errors;

    public class ErrorResponseBuilder
    {
        public static IActionResult GetErrorResponse(ActionContext context)
        {
            string param = GetErrorParam(context);
            string message = GetErrorMessage(context);
            string queryString = context.HttpContext.Request.QueryString.Value;
            string value = GetErrorValue(context, param);
            int statusCode = GetStatusCode(context);

            ErrorResponse response = BuildErrorResponse(message, param, queryString, value, statusCode);

            return BuildActionResultResponse(response);
        }
        
        private static IActionResult BuildActionResultResponse(ErrorResponse response)
        {
            (string responseContent, string type) = FormattedResponseBuilder.GetResponse(response);
            int statusCode = response.ErrorData.First().StatusCode;
            return BuildResponse(responseContent, type, statusCode);
        }
        
        private static ContentResult BuildResponse(string content, string type, int statusCode)
        {
            ContentResult contentResult = new ContentResult();
            contentResult.Content = content;
            contentResult.ContentType = type;
            contentResult.StatusCode = statusCode;

            return contentResult;
        }
        
        private static string GetErrorParam(ActionContext context)
        {
            string parameter = context.ModelState
                .AsEnumerable()
                .FirstOrDefault()
                .Key;
            
            string result = ApiExceptionExtractorHelper.GetExceptionPropByNameWithReflection(context, "Parameter");
            result = StringUtils.ToSnakeCase(result ?? parameter);
            
            return result;
        }
        
        private static string GetErrorMessage(ActionContext context)
        {
            string errorMessage = context.ModelState
                .AsEnumerable()
                .FirstOrDefault()
                .Value
                ?.Errors.FirstOrDefault()?.ErrorMessage;

            if (string.IsNullOrEmpty(errorMessage))
            {
                ObjectResult errorObjectResult = GetObjectResultFromContext(context);
                
                if (errorObjectResult != null)
                {
                    errorMessage = errorObjectResult.Value.ToString();
                }
                else
                {
                    errorMessage = ApiExceptionExtractorHelper.GetExceptionPropByNameWithReflection(context, "Message");
                }
            }

            return errorMessage;
        }
        
        private static string GetErrorValue(ActionContext context, string param)
        {
            string value = context.ModelState
                .AsEnumerable()
                .FirstOrDefault(pair => StringUtils
                    .ToUpperCamelCase(pair.Key)
                    .Equals(StringUtils.ToUpperCamelCase(param), StringComparison.InvariantCultureIgnoreCase))
                .Value?.AttemptedValue;
            
            return value;
        }
        
        private static int GetStatusCode(ActionContext context)
        {
            int statusCode = (int)HttpStatusCode.InternalServerError;
            ModelStateEntry errorModelStateEntry = context.ModelState
                .AsEnumerable()
                .FirstOrDefault()
                .Value;
            
            bool isExceptionContextCastable = typeof(ExceptionContext).IsAssignableFrom(context.GetType());
            
            bool hasPathParamErrors = errorModelStateEntry != null && errorModelStateEntry.Errors.Any();
            bool hasApiException = isExceptionContextCastable && typeof(ApiException).IsAssignableFrom(((ExceptionContext)context).Exception.GetType());
            
            if (hasApiException)
            {
                ObjectResult errorObjectResult = (ObjectResult)((ExceptionContext)context).Result;

                if (errorObjectResult != null)
                {
                    statusCode = errorObjectResult.StatusCode.Value;
                }
            }
            else if (hasPathParamErrors)
            {
                statusCode = (int)HttpStatusCode.BadRequest;
            }
            
            return statusCode;
        }
        
        private static ErrorResponse BuildErrorResponse(
            string message,
            string param,
            string query,
            string value,
            int statusCode)
        {
            JsonErrorResponseData responseData = BuildJsonErrorResponse(message, param, query, value, statusCode);
            ErrorResponse responseError = new ErrorResponse()
            {
                ErrorData = new List<JsonErrorResponseData>()
                {
                    responseData
                }
            };

            return responseError;
        }
        
        private static ObjectResult GetObjectResultFromContext(ActionContext context)
        {
            ObjectResult errorObjectResult = null;

            try
            {
                errorObjectResult = (ObjectResult)((ExceptionContext)context).Result;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"{ex.Message} in function: {MethodBase.GetCurrentMethod()?.Name}");
            }

            return errorObjectResult;
        }
        
        private static JsonErrorResponseData BuildJsonErrorResponse(
            string message,
            string parameter,
            string queryString,
            string value,
            int code)
        {
            return new JsonErrorResponseData()
            {
                Message = message,
                Parameter = parameter,
                Query = queryString,
                Value = value,
                StatusCode = code
            };
        }
    }
}