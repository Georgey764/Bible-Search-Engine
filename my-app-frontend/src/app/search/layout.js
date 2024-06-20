"use client"

import Image from "next/image";
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { useEffect, useState } from "react"
import { useRouter } from "next/navigation";
import { useSearchParams } from 'next/navigation'

export default function SearchLayout({children}) {
  const searchParams = useSearchParams()
  const [query, setQuery] = useState(searchParams.get("query"))
  const router = useRouter();

  function handleInput(e) {
    setQuery(e.target.value);
  }

  function handleInput(e){
    setQuery(e.target.value)
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between">
      <div className="cursor-pointer bg-white z-10 fixed w-full p-4 border-b flex flex-row item-center justify-center gap-2">
        <span onClick={e => router.push(`/`)} className="flex flex-row item-center justify-center gap-2">
          <div style={{position:"relative"}} className="w-[30px] h-[30px]">
            <Image
              src="/bible.png"
              alt="Picture of the bible"
              layout={'fill'} 
              objectFit={'contain'}
            />
          </div>
        <h1 className="m-0 font-bold text-2xl">Search Bible</h1>
        </span>
        <form onSubmit={(e) => {
          e.preventDefault()
          router.push(`/search?query=${query}`)
        }} className="ml-4">
          <div className="flex flex-row gap-2" >
            <Input placeholder="Search for 2001 Translation Bible verses..." value={query} onChange={handleInput} style={{width:"max(30vw, 200px)"}} />
            <Button>Search</Button>
          </div>
        </form>
      </div>
      {children}
    </main>
  );
}
