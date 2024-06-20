import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react"

export default function SearchCard({book, chapter, bm25, query}){
  const router = useRouter();
  const [previewText, setPreviewText] = useState("")

  useEffect(()=>{
    let url = `http://localhost:8080/text-preview?book=${book}&chapter=${chapter}&query=${encodeURIComponent(query)}`
    fetch(url)
      .then(res => res.text())
      .then(data => setPreviewText(data.slice(0, 50) + "..." ))
      .catch(err => console.log(err))
  },[])

  return (
      <Card style={{width: "max(50vw, 300px)"}}>
        <div className="flex flex-row justify-between">  
          <CardHeader>
            <CardTitle>{book}</CardTitle>
            <CardDescription>Chapter {chapter}</CardDescription>
          </CardHeader>
          <CardContent className="p-6">
            <p>Search Score: {bm25}</p>
          </CardContent>
        </div>
        <div className="flex flex-row justify-between">  
          <CardContent>
            <p>{previewText}</p>
          </CardContent>
          <CardContent 
            onClick={(e) => {
              e.preventDefault()
              router.push(`/search/chapter?book=${book}&chapter=${chapter}&query=${query}`)
            }} 
            className="text-blue-500 hover:text-blue-700 cursor-pointer">
            <p>Read...</p>
          </CardContent>
        </div>
        {/* <CardFooter>
          <p>Card Footer</p>
        </CardFooter> */}
      </Card>
    );
}