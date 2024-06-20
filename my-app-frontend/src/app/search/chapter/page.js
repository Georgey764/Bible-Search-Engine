"use client"
import { useEffect, useState } from "react"
import { useSearchParams } from 'next/navigation'

export default function SearchCard(){
  const [text, setText] = useState([])
  const [keywords_indices, set_keyword_indices] = useState({})
  const lineSet = new Set(Object.keys(keywords_indices))
  const [previewIndices, setPreviewIndices] = useState("")

  const searchParams = useSearchParams()
  const book = searchParams.get('book')
  const chapter = searchParams.get('chapter')
  const query = searchParams.get('query')
  
  useEffect(()=>{
    Promise.all([
        fetch(`http://localhost:8080/keyword-indices?book=${book}&chapter=${chapter}&query=${query}`),
        fetch(`http://localhost:8080/preview-indices?book=${book}&chapter=${chapter}&query=${query}`),
        fetch(`http://localhost:8080/chapter?book=${book}&chapter=${chapter}`)
      ])
      .then(lists => {
        return Promise.all([lists[0].json(), lists[1].json(), lists[2].json()]);
      })
      .then(data => {
        set_keyword_indices(data[0])
        setPreviewIndices(data[1])
        setText(data[2])
      })
      .catch(err => console.log(err))
  },[])

  return (
    <div className="p-10 my-8">
      {
        text.map((cur, i) => {     
            let result = cur.length == 0 ? <div key={i+cur}><br/></div> : cur
            result = [0,1,2].includes(i) ? <div key={i+cur}><p key={cur + cur + i} className="font-bold text-2xl text-center">{cur}</p><br/></div> : result;
            if (lineSet.has(i.toString())){
              let indices = keywords_indices[i];
              result = cur.split(/[ \t]+/).map((wor, index) => {
                return indices.includes(index) ? <span key={wor + index + cur}><span key={ index + wor + i + cur} className="bg-slate-300">{wor}</span>{" "}</span> : <span key={ index + wor + i + cur}>{wor}{" "}</span>
              })
            }
            if (previewIndices[0] == i){
              result = <span key={i+cur} className="bg-red-300">{cur}</span>
            }
            return result;
          }
        )
      }
    </div>)
}