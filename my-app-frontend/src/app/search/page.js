"use client"

import Image from "next/image";
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import SearchCard from "./(components)/Card.js"
import { Skeleton } from "@/components/ui/skeleton"
import { useState, useEffect } from "react"
import { useSearchParams } from 'next/navigation'

export default function SearchPage() {
  const [loading, setLoading] = useState(true)
  const [bm25_scores, set_bm25_scores] = useState(new Array(20).fill(0))
  const searchParams = useSearchParams()
  const query = searchParams.get('query')

  function handleSubmit(e){
    e.preventDefault()
    const url_get = `http://localhost:8080/read/${query}`
    fetch(url_get)
      .then(res => res.json())
      .then(data => {
        set_bm25_scores(data)
        setLoading(false)
      })
      .catch(e => console.log(e))
  }

  useEffect(()=>{
    setLoading(true)
    const url_get = `http://localhost:8080/read/${query}`
    fetch(url_get)
      .then(res => res.json())
      .then(data => {
        set_bm25_scores(data)
        setLoading(false)
      })
      .catch(e => console.log(e))
  }, [query])

  let first_search = bm25_scores.slice(0, 20)

  return (
    <main className="flex min-h-screen flex-col items-center justify-between">
      <div className="flex flex-col gap-4 my-24" style={{width: "max(50vw, 300px)"}}>
      <p className="text-sm font-light text-center">Please make sure you are searching for VERSES from 2001 translation of the Bible</p>
        <p className="text-center text-lg font-light">The following 2001 translation Bible chapters best match the given verse:</p>
        {
          loading ? 
            (bm25_scores.map((cur, i) => <div key={cur + i} className="p-4 flex flex-col items-start space-y-3" style={{width: "max(50vw, 300px)"}}>
                          <div className="flex flex-row justify-between w-full">
                            <Skeleton className="h-6 w-[250px] rounded-xl" />
                            <Skeleton className="h-4 w-[50px] rounded-xl" />
                          </div>
                          <div className="space-y-2 w-full">
                            <Skeleton className="h-4 w-[200px]" />
                            <Skeleton className="h-4 w-[150px]" />
                            <div className="flex flex-row justify-between w-full">
                              <Skeleton className="h-4 w-[150px]" />
                              <Skeleton className="h-4 w-[100px] rounded-xl" />
                            </div>
                          </div>
                        </div>))
           : 
            first_search.map(
                          cur => <SearchCard 
                                  book={cur[0].split("_")[0]} 
                                  chapter={cur[0].split("_")[2].split(".")[0]}
                                  bm25={Math.round(cur[1] * 100) / 100}
                                  query={query}
                                  key={cur}/>
                        )
              
        }
      </div>
    </main>
  );
}
