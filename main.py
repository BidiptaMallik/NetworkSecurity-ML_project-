from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.datat_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        training_pipeline=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(training_pipeline)
        
        dataingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiated the data ingestion")
        
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(training_pipeline)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("initiate data validation")
        data_validation.initiate_data_validation
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info('Data Validation completed')
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(training_pipeline)
        logging.info("Data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)