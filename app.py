import { useState } from 'react'
import { Upload, AlertCircle, Github, Linkedin, Mail } from 'lucide-react'
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"

export default function DiabetesRetinopathyDetection() {
  const [file, setFile] = useState<File | null>(null)
  const [imagePreview, setImagePreview] = useState<string | null>(null)
  const [prediction, setPrediction] = useState<string | null>(null)
  const [suggestions, setSuggestions] = useState<string | null>(null)
  const [remedy, setRemedy] = useState<string | null>(null)

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file) {
      setFile(file)
      const reader = new FileReader()
      reader.onloadend = () => {
        setImagePreview(reader.result as string)
      }
      reader.readAsDataURL(file)
    }
  }

  const handlePredict = async () => {
    // This is where you'd typically make an API call to your backend
    // For demonstration, we'll use mock data
    const mockPrediction = Math.floor(Math.random() * 5)
    const results = getPredictionResults(mockPrediction)
    setPrediction(results.message)
    setSuggestions(results.suggestions)
    setRemedy(results.remedy)
  }

  const getPredictionResults = (prediction: number) => {
    switch(prediction) {
      case 0:
        return {
          message: "No Diabetic Retinopathy detected.",
          suggestions: "Maintain regular eye check-ups.",
          remedy: ""
        }
      case 1:
        return {
          message: "Mild Diabetic Retinopathy detected.",
          suggestions: "Consider lifestyle changes such as diet and exercise.",
          remedy: "Consult an ophthalmologist for further evaluation."
        }
      case 2:
        return {
          message: "Moderate Diabetic Retinopathy detected.",
          suggestions: "Regular monitoring is essential.",
          remedy: "Discuss treatment options with your healthcare provider."
        }
      case 3:
        return {
          message: "Severe Diabetic Retinopathy detected.",
          suggestions: "Immediate medical attention is required.",
          remedy: "Follow up with a specialist urgently."
        }
      case 4:
        return {
          message: "Proliferative Diabetic Retinopathy detected.",
          suggestions: "Urgent intervention is necessary.",
          remedy: "Seek treatment from a retinal specialist immediately."
        }
      default:
        return {
          message: "Unable to determine.",
          suggestions: "Please consult with a healthcare professional.",
          remedy: ""
        }
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md mx-auto">
        <div className="text-center mb-8">
          <img src="/placeholder.svg?height=100&width=100" alt="Logo" className="mx-auto h-24 w-24" />
          <h2 className="mt-6 text-3xl font-extrabold text-gray-900">
            Diabetic Retinopathy Detection
          </h2>
        </div>
        
        <Card>
          <CardHeader>
            <CardTitle>Upload Retinal Image</CardTitle>
            <CardDescription>Choose a retinal image for analysis</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex items-center justify-center w-full">
              <label htmlFor="dropzone-file" className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100">
                <div className="flex flex-col items-center justify-center pt-5 pb-6">
                  <Upload className="w-10 h-10 mb-3 text-gray-400" />
                  <p className="mb-2 text-sm text-gray-500"><span className="font-semibold">Click to upload</span> or drag and drop</p>
                  <p className="text-xs text-gray-500">PNG or JPG (MAX. 800x400px)</p>
                </div>
                <input id="dropzone-file" type="file" className="hidden" onChange={handleFileChange} accept="image/*" />
              </label>
            </div>
            {imagePreview && (
              <div className="mt-4">
                <img src={imagePreview} alt="Preview" className="max-w-full h-auto rounded-lg" />
              </div>
            )}
          </CardContent>
          <CardFooter>
            <Button className="w-full" onClick={handlePredict} disabled={!file}>
              Predict
            </Button>
          </CardFooter>
        </Card>

        {prediction && (
          <Alert className="mt-8">
            <AlertCircle className="h-4 w-4" />
            <AlertTitle>Prediction Result</AlertTitle>
            <AlertDescription>
              {prediction}
              {suggestions && (
                <>
                  <h4 className="font-semibold mt-2">Suggestions:</h4>
                  <p>{suggestions}</p>
                </>
              )}
              {remedy && (
                <>
                  <h4 className="font-semibold mt-2">Remedies:</h4>
                  <p>{remedy}</p>
                </>
              )}
            </AlertDescription>
          </Alert>
        )}

        <footer className="mt-8 text-center">
          <h3 className="text-lg font-semibold mb-2">Contact Me</h3>
          <div className="flex justify-center space-x-4">
            <a href="https://github.com/Heet852003" target="_blank" rel="noopener noreferrer">
              <Github className="h-6 w-6" />
            </a>
            <a href="https://www.linkedin.com/in/heet-mehta-41b862225" target="_blank" rel="noopener noreferrer">
              <Linkedin className="h-6 w-6" />
            </a>
            <a href="mailto:mehtaheet5@gmail.com">
              <Mail className="h-6 w-6" />
            </a>
          </div>
        </footer>
      </div>
    </div>
  )
}
