/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "fatfs.h"
#include "sdio.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "retarget.h"
#include "string.h"
#include <stdio.h>
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  MX_SDIO_SD_Init();
  MX_FATFS_Init();
  /* USER CODE BEGIN 2 */

  RetargetInit(&huart1);
  printf("[INFO] Starting SDIO peripheral demo\n");

  if (f_mount(&SDFatFS, SDPath, 1) != FR_OK) {
    printf("[INFO] Mount fatfs Fail\n");
    Error_Handler();
  }
  printf("[INFO] Mount sd Success\n");
  
  HAL_SD_CardCIDTypeDef    pCID;
  HAL_SD_CardCSDTypeDef    pSID;
  HAL_SD_CardStatusTypeDef pStatus;
  HAL_SD_CardInfoTypeDef   pCardInfo;

  if (HAL_SD_GetCardCID(&hsd, &pCID) != HAL_OK)
    Error_Handler();

  if (HAL_SD_GetCardCSD(&hsd, &pSID) != HAL_OK)
    Error_Handler();

  if (HAL_SD_GetCardStatus(&hsd, &pStatus) != HAL_OK)
    Error_Handler();

  if (HAL_SD_GetCardInfo(&hsd, &pCardInfo) != HAL_OK)
    Error_Handler();

  printf("[INFO[ ==== CID ====\n");
  printf("[INFO] pCID.ManufacturerID = %d\n", pCID.ManufacturerID);
  printf("[INFO] pCID.OEM_AppliID = %d\n", pCID.OEM_AppliID);
  printf("[INFO] pCID.ProdName %s%s\n", (char*) &pCID.ProdName1, (char*) &pCID.ProdName2);
  printf("[INFO] pCID.ProdRev = %d\n", pCID.ProdRev);
  printf("[INFO] pCID.ProdSN = %ld\n", pCID.ProdSN);
  printf("[INFO] pCID.ManufactDate = 0x%04X\n", pCID.ManufactDate);
  printf("[INFO] pCID.CID_CRC = 0x%02X\n", pCID.CID_CRC);

  printf("[INFO[ ==== SID ====\n");
  printf("[INFO] pSID.SysSpecVersion = %d\n", pSID.SysSpecVersion);
  printf("[INFO] pSID.CardComdClasses = %d\n", pSID.CardComdClasses);
  printf("[INFO] pSID.DeviceSize = %ld\n", pSID.DeviceSize);
  printf("[INFO] pSID.DeviceSizeMul = %d\n", pSID.DeviceSizeMul);
  printf("[INFO] pSID.MaxBusClkFrec = %d\n", pSID.MaxBusClkFrec);
  printf("[INFO] pSID.TAAC (read time) = %d\n", pSID.TAAC);
  printf("[INFO] pSID.RdBlockLen = %d\n", pSID.RdBlockLen);
  printf("[INFO] pSID.MaxWrBlockLen = %d\n", pSID.MaxWrBlockLen);
  printf("[INFO] pSID.EraseGrSize = %d\n", pSID.EraseGrSize);
  printf("[INFO] pSID.EraseGrMul = %d\n", pSID.EraseGrMul);
  printf("[INFO] pSID.WrProtectGrSize = %d\n", pSID.EraseGrSize);
  printf("[INFO] pSID.WrProtectGrEnable = %d\n", pSID.WrProtectGrEnable);

  printf("[INFO[ ==== Status ====\n");
  printf("[INFO] pStatus.DataBusWidth = %d\n", pStatus.DataBusWidth);
  printf("[INFO] pStatus.SecuredMode = %d\n", pStatus.SecuredMode);
  printf("[INFO] pStatus.CardType = %d\n", pStatus.CardType);
  printf("[INFO] pStatus.ProtectedAreaSize = %ld\n", pStatus.ProtectedAreaSize);
  printf("[INFO] pStatus.SpeedClass = %d\n", pStatus.SpeedClass);
  printf("[INFO] pStatus.PerformanceMove = %d\n", pStatus.PerformanceMove);
  printf("[INFO] pStatus.AllocationUnitSize = %d\n", pStatus.AllocationUnitSize);
  printf("[INFO] pStatus.EraseSize = %d\n", pStatus.EraseSize);
  printf("[INFO] pStatus.EraseTimeout = %d\n", pStatus.EraseTimeout);
  printf("[INFO] pStatus.EraseOffset = %d\n", pStatus.EraseOffset);

  printf("[INFO[ ==== CardInfo ====\n");
  printf("[INFO] pCardInfo.CardType = %ld\n", pCardInfo.CardType);
  printf("[INFO] pCardInfo.CardVersion = %ld\n", pCardInfo.CardVersion);
  printf("[INFO] pCardInfo.Class = %ld\n", pCardInfo.Class);
  printf("[INFO] pCardInfo.RelCardAdd = %ld\n", pCardInfo.RelCardAdd);
  printf("[INFO] pCardInfo.BlockNbr = %ld\n", pCardInfo.BlockNbr);
  printf("[INFO] pCardInfo.BlockSize = %ld\n", pCardInfo.BlockSize);
  printf("[INFO] pCardInfo.LogBlockNbr = %ld\n", pCardInfo.LogBlockNbr);
  printf("[INFO] pCardInfo.LogBlockSize = %ld\n", pCardInfo.LogBlockSize);

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  char buff[16] = {0};
  UINT br, bw;

  if (f_open(&SDFile, "test.txt", FA_OPEN_EXISTING | FA_READ) != FR_OK)
    Error_Handler();
  printf("[INFO] Open file Success\n");

  retSD = f_read(&SDFile, buff, 4, &br);
  if (retSD != FR_OK) {
    printf("[INFO] f_write return value (%d) \n", retSD);
    Error_Handler();
  }
  printf("[INFO] Read file content: %s\n", buff);  
  
  if (f_close(&SDFile) != FR_OK)
    Error_Handler();
  printf("[INFO] Close file Success\n");

  
  if (f_open(&SDFile, "test.bak", FA_WRITE | FA_CREATE_ALWAYS) != FR_OK) {
    Error_Handler();
  }
  printf("[INFO] Create file Success\n");

  if (f_write(&SDFile, buff, 4, &bw) != FR_OK)
    Error_Handler();
  printf("[INFO] Write file Success\n");

  if (f_close(&SDFile) != FR_OK)
    Error_Handler();
  printf("[INFO] STM32 SDIO DEMO END\n");
  
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);
  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 8;
  RCC_OscInitStruct.PLL.PLLN = 50;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 4;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_1) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
