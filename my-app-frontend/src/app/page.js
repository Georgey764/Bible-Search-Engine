"use client";

import Image from "next/image";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const [query, setQuery] = useState("");
  const router = useRouter();

  function handleInput(e) {
    setQuery(e.target.value);
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between">
      <div className="h-screen w-screen text-center flex flex-col items-center justify-center gap-8">
        <div className="flex flex-row gap-2">
          <h1 className="m-0 font-bold text-4xl">Search Bible</h1>
          <div style={{position:"relative"}} className="w-[38px] h-[38px]">
            <Image
              src="/bible.png"
              alt="Picture of the bible"
              layout={'fill'} 
              objectFit={'contain'}
            />
          </div>
        </div>
        <form onSubmit={(e) => {
          e.preventDefault()
          router.push(`/search?query=${query}`)
        }}>
          <div className="flex flex-row gap-2">
            <Input
              placeholder="Search for 2001 Translation Bible verses..." 
              value={query}
              onChange={handleInput}
              style={{ width: "max(40vw, 200px)" }}
            />
            <Button>Search</Button>
          </div>
        </form>
        <p className="text-sm font-light text-center">Please make sure you are searching for VERSES from 2001 translation of the Bible</p>
        <div className="flex flex-row gap-2">
          <Button variant="outline">Blog</Button>
          <Button variant="outline">Options</Button>
        </div>
      </div>
    </main>
  );
}
