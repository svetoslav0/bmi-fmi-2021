namespace KidneyCarcinomaRestApi
{
    using Microsoft.AspNetCore.Builder;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.Extensions.Configuration;
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.Extensions.Hosting;

    using KidneyCarcinomaRestApi.Interfaces;
    using KidneyCarcinomaRestApi.Models;

    using MongoDB.Driver;

    using KidneyCarcinomaRestApi.Services;
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();

            IConfigurationSection mongoConfig = Configuration.GetSection("MongoDb");

            string mongoConnectionString = mongoConfig.GetValue<string>("ConnectionUri");
            string databaseName = mongoConfig.GetValue<string>("DatabaseName");
            string diagnosesCollectionName = mongoConfig.GetValue<string>("DiagnosesCollectionName");
            string casesCollectionName = mongoConfig.GetValue<string>("CasesCollectionName");
            
            MongoClient mongoClient = new MongoClient(mongoConnectionString);
            IMongoDatabase database = mongoClient.GetDatabase(databaseName);
            
            IMongoCollection<Diagnose> diagnosesCollection = database.GetCollection<Diagnose>(diagnosesCollectionName);
            IMongoCollection<Case> casesCollection = database.GetCollection<Case>(casesCollectionName);
            
            IDiagnosisService diagnosisService = new DiagnosiService(diagnosesCollection);
            ICasesService casesService = new CasesService(casesCollection);

            services.AddSingleton(diagnosisService);
            services.AddSingleton(casesService);
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseHttpsRedirection();

            app.UseRouting();

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }
    }
}
