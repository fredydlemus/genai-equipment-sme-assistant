data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "../lambda_function.py"
  output_path = "lambda_function.zip"
}

resource "aws_lambda_function" "equipment_sme_assitant" {
  function_name = "equipment_sme_assitant"
  role          = aws_iam_role.lambda_execution_role.arn
  filename      = data.archive_file.lambda_zip.output_path
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  timeout       = 120

  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
}
